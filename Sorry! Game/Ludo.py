
# Leandro H. G. Aguiar, ThankGod Ofurum, Franck Dosso

#generate sound for panel

import pygame, time, sys, random
from pygame.locals import *
from GameSound import *
import os
import ctypes

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (210, 30, 30)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (220, 220, 30)
COLORS = [GREEN, RED, BLUE, YELLOW]
GREY = (100, 100, 100)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
# set up the spot sizes and number of spots
RECT_WIDTH = int(user32.GetSystemMetrics(0) / 15)
RECT_HEIGHT = int(user32.GetSystemMetrics(1) / 15)
# game step macros
DIE_ROLLING = 1
PAWN_MOVE = 2

#initialize sound
pygame.init()
pygame.mixer.init()
sound = soundGallery()

class ludo_tile():
    "Spot class"
    def __init__(self, left, top, width, height, row, column, color=WHITE):
        "Init"
        self.rect = pygame.Rect(left, top, width, height)
        self.row = row
        self.column = column
        self.color = color


class ludo_pawn(ludo_tile):
    "Piece class"
    def __init__(self, left, top, width, height, row, column, color, spot_number, first_spot):
        "Init"
        self.rect = pygame.Rect(left, top, width, height)
        self.row = row
        self.column = column
        self.color = color
        self.spot_number = spot_number
        self.home_row = row
        self.home_col = column
        self.first_spot = first_spot
        self.spots_traveled = 0
        self.is_in_finalpath = 0

    def move(self, num_spots, spots_set, finalpath_set):
        "Move the pieces through the board"
        if (self.is_in_finalpath == 0):
            # Update spot number and number of spots traveled
            self.spots_traveled += num_spots
            sound.play_move()
            if (self.spots_traveled >= (len(spots_set) - 1)):
                # Entered final path
                self.is_in_finalpath = 1
                self.spot_number = self.spots_traveled - (len(spots_set) - 1)
                sound.play_suspens()
                # Update positioning variables
                self.row = finalpath_set[self.spot_number].row
                self.rect.top = finalpath_set[self.spot_number].rect.top
                self.column = finalpath_set[self.spot_number].column
                self.rect.left = finalpath_set[self.spot_number].rect.left
                sound.play_move()
            else:
                # Not entering final path - Update the spot number
                self.spot_number = (self.spot_number + num_spots) % len(spots_set)
                sound.play_move()
                # Update positioning variables
                self.row = spots_set[self.spot_number].row
                self.rect.top = spots_set[self.spot_number].rect.top
                self.column = spots_set[self.spot_number].column
                self.rect.left = spots_set[self.spot_number].rect.left
                sound.play_move()
        else:
            # Update the spot number
            aux = (self.spot_number + num_spots) // (len(finalpath_set) - 1)
            if (aux == 0):
                self.spot_number = self.spot_number + num_spots
            else:
                self.spot_number = (len(finalpath_set) - 1)
            # Update positioning variables
            self.row = finalpath_set[self.spot_number].row
            self.rect.top = finalpath_set[self.spot_number].rect.top
            self.column = finalpath_set[self.spot_number].column
            self.rect.left = finalpath_set[self.spot_number].rect.left
            sound.finish_line() #(not sure)
           

    def leave_home(self, spots_set):
        "Leave the home groud. Pawn is moved to its first position"
        # Update variables
        self.row = spots_set[self.first_spot].row
        self.rect.top = spots_set[self.first_spot].rect.top
        self.column = spots_set[self.first_spot].column
        self.rect.left = spots_set[self.first_spot].rect.left
        self.spot_number = self.first_spot
        sound.get_out()

    def goback_home(self):
        "Move the pawn back to its home position"
        # Update variables
        self.row = self.home_row
        self.rect.top = self.row * RECT_WIDTH
        self.column = self.home_col
        self.rect.left = self.column * RECT_HEIGHT
        self.spot_number = -1
        self.spots_traveled = 0
        sound.black_hole()

    def is_in_deep_pit(self, board_spots):
        "Check if the piece is in a deep pit. \
         Returns false if it`s not or if the other \
         pieces have caugh up."
        for i in range(len(board_spots)):
            if (board_spots[i].color == GREY and self.row == board_spots[i].row \
                      and self.column == board_spots[i].column):
                return True
        return False

    def is_in_black_hole(self, board_spots):
        "Check if the piece is in a black hole"
        for i in range(len(board_spots)):
            if (board_spots[i].color == BLACK and self.row == board_spots[i].row \
                      and self.column == board_spots[i].column):
                return True
        return False

class player(object):
    "Player class"
    def __init__(self, color):
        self.color = color
        self.pawns = []
        self.final_path = []

class Game():
    "Class that runs the game"
    def __init__(self, num_players, num_humans, num_pawns, num_finish):
        "Do some work."
        # Initialize the user inputs
        self.num_players = int(num_players)
        self.num_humans = int(num_humans)
        self.num_pawns = int(num_pawns)
        self.num_finish = int(num_finish)
        # Initialize the board dimensions
        self.num_cols = 15
        self.num_rows = 15
        self.window_width = RECT_WIDTH * self.num_cols
        self.window_height = RECT_HEIGHT * self.num_rows
        # set up pygame
        pygame.init()
        self.mainClock = pygame.time.Clock()
        # set up the window
        self.windowSurface = pygame.display.set_mode((self.window_width, self.window_height), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        pygame.display.set_caption('Ludo')
        # set up the board image
        self.board_img = pygame.image.load(os.path.join('img','board_ludo.gif'))
        self.board_img = pygame.transform.scale(self.board_img, \
                             (self.window_width, self.window_height))
        # Initialize the spots
        # Open the board configuration file
        board_file = open(os.path.join('cfg', 'board_cfg.txt'), 'r')
        board_spots = []
        for line in board_file:
            board_spots.append([int(x) for x in line.split()])
        board_file.close()
        # Create a list with the board spots
        self.spots = []
        for [column, row] in board_spots:
            row = (self.num_rows - 1) - row # Translate coordinates from 1 to 4 quadrant
            new_spot = ludo_tile(column*RECT_WIDTH, row*RECT_HEIGHT, \
                               RECT_WIDTH, RECT_HEIGHT, row, column)
            self.spots.append(new_spot)
        # Initialize the players
        self.players = []
        self.initialize_players()
        # Initialize the sound
        pygame.mixer.init()
        self.sound = soundGallery()
        self.music = musicGallery()
        # Play the theme song
        self.music.load_themesong()
        self.music.set_volume(0.06)
        self.music.play_song(-1) # -1 means play forever

    def position_deep_pits(self):
        "Position the deep pits in the board"
        #print("Click on the spots in which you want to position deep pits")
        pygame.time.delay(2000)
        sound.say_dpits()
        while True:
            # Check events
            for event in pygame.event.get():
                # Check for Quit event
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # Check for thee mouse click event
                if event.type == MOUSEBUTTONUP:
                    for i in range(len(self.spots)):
                        if (self.spots[i].rect.collidepoint(event.pos)):
                            if (self.spots[i].color == WHITE):
                                self.spots[i].color = GREY
                                print("Deep pit positioned")
                            elif (self.spots[i].color == GREY):
                                self.spots[i].color = WHITE
                                print("Deep pit removed")
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    # Done with the black holes
                    if (event.key == K_KP_ENTER or event.key == K_RETURN):
                        print("Done with the deep pits positioning")
                        return
            self.update_screen()

    def position_black_holes(self):
        "Position the black holes in the board"
        #print("Click on the spots in which you want to position black holes")
        sound.stop_sound()
        sound.say_bholes()
        while True:
            # Check events
            for event in pygame.event.get():
                # Check for Quit event
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                # Check for thee mouse click event
                if event.type == MOUSEBUTTONUP:
                    for i in range(len(self.spots)):
                        if (self.spots[i].rect.collidepoint(event.pos)):
                            if (self.spots[i].color == WHITE):
                                self.spots[i].color = BLACK
                                print("Black hole positioned")
                            elif (self.spots[i].color == BLACK):
                                self.spots[i].color = WHITE
                                print("Black hole removed")
                            elif (self.spots[i].color == GREY):
                                self.spots[i].color = BLACK
                                print("Deep pit removed")
                                print("Black hole positioned")
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    # Done with the black holes
                    if (event.key == K_KP_ENTER or event.key == K_RETURN):
                        print("Done with the black holes positioning")
                        sound.stop_sound()
                        sound.say_rollit()
                        #put rollit maybe here
                        return
            self.update_screen()

    def initialize_players(self):
        "Initialize the players and position their pawns"
        # Open start points file
        startpt_file = open(os.path.join('cfg', 'startpt_cfg.txt'), 'r')
        # Open final paths file
        finalpath_file = open(os.path.join('cfg', 'finalpath_cfg.txt'), 'r')
        # For each player
        for plr_no in range(self.num_players):
            # Create player and add him to the vector
            new_player = player(plr_no)
            self.players.append(new_player)
            # Read the player's pawns final path positions
            for i in range(6): #FIXME 6 HARDCODED
                # Read the position of each spot
                line = finalpath_file.readline()
                pos = [int(x) for x in line.split()]
                col = pos[0]
                row = (self.num_rows - 1) - pos[1] # Change coordinates from 1 to 4 quadrant
                left = col * RECT_WIDTH
                top = row * RECT_HEIGHT
                # Add spot to the player's final path
                new_spot = ludo_tile(left, top, RECT_WIDTH, RECT_HEIGHT, \
                          row, col, COLORS[plr_no])
                self.players[plr_no].final_path.append(new_spot)
            # For each pawn
            pawns = 0
            # Read the position of each
            while (pawns < self.num_pawns):
                # Read the start position of the pawn
                line = startpt_file.readline()
                pos = [int(x) for x in line.split()]
                col = pos[0]
                row = (self.num_rows - 1) - pos[1] # Change coordinates from 1 to 4 quadrant
                left = col * RECT_WIDTH
                top = row * RECT_HEIGHT
                # Add the pawn to the player's set
                new_piece = ludo_pawn(left, top, RECT_WIDTH, RECT_HEIGHT, \
                        row, col, COLORS[plr_no], -1, (1 + plr_no * 13)) #FIXME 13 HARDCODED
                self.players[plr_no].pawns.append(new_piece)
                pawns = pawns + 1
            # Skip the next lines from this player if num_pawns < 4 - FIXME: MAX_PLAYERS
            while (pawns < 4):
                line = startpt_file.readline()
                pawns = pawns + 1
        # Close the start points file
        startpt_file.close()

    def run(self):
        "It runs the game."
        die = 0
        step = DIE_ROLLING
        #print("Press enter to roll the die.")
        # run the game loop
        while True:
         for plr_no in range(self.num_players):
          done = 0
          while (not done):
            # Rolling the die
            if step == DIE_ROLLING:
                # check for events
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        # roll the die
                        if (event.key == K_KP_ENTER or event.key == K_RETURN) and die == 0:
                            sound.stop_sound()
                            sound.play_dice() #sound of die
                            die = random.randrange(1, 7)
                            if (die == 1):
                                sound.say_one()
                            if die ==2:
                                sound.say_two()
                            if die == 3:
                                sound.say_three()
                            if die == 4:
                                sound.say_four()
                            if die == 5:
                                sound.say_five()
                            if die == 6:
                                sound.say_six()
                                
                            print("Die rolled. You got a " + str(die) + ".")
                            if self.piece_available_move(plr_no, die):
                                pygame.time.delay(1000)
                                print("Click on the piece to be moved.")
                                sound.click_move()
                                step = PAWN_MOVE
                            else:
                                print("No movements are possible.")
                                pygame.time.delay(1800)
                                sound.no_move()
                                print("Press enter to roll the die.")
                                die = 0
                                step = DIE_ROLLING
                                done = 1
            # Doing forward move
            elif step == PAWN_MOVE:
                # check for events
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.type == MOUSEBUTTONUP:
                        for i in range(len(self.players[plr_no].pawns)):
                            if (self.players[plr_no].pawns[i].rect.collidepoint(event.pos) \
                                        and (((not self.players[plr_no].pawns[i].\
                                        is_in_deep_pit(self.spots) and self.players[plr_no].\
                                        pawns[i].spot_number != -1) or (die == 6)) \
                                        and not (self.players[plr_no].pawns[i].\
                                        is_in_finalpath != 0 and self.players[plr_no].pawns[i].\
                                        spot_number == 5))):
                                if (self.players[plr_no].pawns[i].spot_number == -1):
                                    self.players[plr_no].pawns[i].leave_home(self.spots)
                                else:
                                    self.players[plr_no].pawns[i].move(die, self.spots, \
                                                        self.players[plr_no].final_path)
                                # check if piece was moved into a black hole
                                if self.players[plr_no].pawns[i].is_in_black_hole(self.spots):
                                    print("Moved into a black hole.")
                                    self.players[plr_no].pawns[i].goback_home()
                                # check if the pawn landed over another player's one
                                else:
                                    self.check_send_home(plr_no, \
                                               self.players[plr_no].pawns[i].spot_number, i)
                                # check if someone won the game
                                winner = self.check_win()
                                if (winner != 0):
                                    print("Player " + str(winner) + " won the game!")
                                    sound.say_ovation()
                                    pygame.time.delay(5000)
                                    sound.say_won()
                                    music.load_winSong()
                                    music.stop_music()
                                    music.play_song(-1)
                                    return
                                # update variables for next turn
                                print("Press enter to roll the die.")
                                die = 0
                                step = DIE_ROLLING
                                done = 1
                                break
            self.update_screen()

    def piece_available_move(self, plr_no, die):
        "Check if there are pieces available to be moved"
        count = 0
        for i in range(len(self.players[plr_no].pawns)):
            if ((die == 6 or (not self.players[plr_no].pawns[i].is_in_deep_pit(self.spots) \
                        and self.players[plr_no].pawns[i].spot_number != -1)) \
                        and not ((self.players[plr_no].pawns[i].spot_number == 5) \
                        and (self.players[plr_no].pawns[i].is_in_finalpath != 0))):
                count += 1
        return count

    def check_send_home(self, player_num, spot_num, pawn_num):
        "Check if the pawn is landed over another player's one"
        for plr_no in range(self.num_players):
            # Only send back other player's pawns
            if (plr_no != player_num):
                for i in range(len(self.players[plr_no].pawns)):
                    # If on the same spot, send it back home
                    if ((not self.players[player_num].pawns[pawn_num].is_in_finalpath) \
                                and (not self.players[plr_no].pawns[i].is_in_finalpath) \
                                and (self.players[plr_no].pawns[i].spot_number == spot_num)):
                        self.players[plr_no].pawns[i].goback_home()
                        print("Sent player " + str(plr_no + 1) + "'s pawn back home!")

    def check_win(self):
        "Check if someone won the game"
        for plr_no in range(self.num_players):
            ended = 0
            for i in range(len(self.players[plr_no].pawns)):
                if (self.players[plr_no].pawns[i].is_in_finalpath != 0 \
                            and self.players[plr_no].pawns[i].spot_number == 5): #FIXME 5 HARD
                    ended += 1
            if (ended >= self.num_finish):
                return (plr_no + 1)
        return 0

    def update_screen(self):
        "Updates the screen"
        # draw the board background onto the surface
        self.windowSurface.blit(self.board_img, (0, 0))
        # draw the pits
        for i in range(len(self.spots)):
            if (self.spots[i].color != WHITE):
                pygame.draw.rect(self.windowSurface, self.spots[i].color, self.spots[i].rect)
        # draw the pawns
        for plr_no in range(self.num_players):
            for i in range(len(self.players[plr_no].pawns)):
                pygame.draw.circle(self.windowSurface, self.players[plr_no].pawns[i].color, \
                                            self.players[plr_no].pawns[i].rect.center, 20)
        # draw the window onto the screen
        pygame.display.update()
        self.mainClock.tick(50)


def is_num_in_range(user_input, min_val, max_val):
    "Check if the user input is a number and if it is in [min_val max_val] range"
    try:
        val = int(user_input)
    except ValueError:
        return False
    if (val >= min_val and val <= max_val):
        return True
    else:
        return False


if __name__ == "__main__":
    "Main function. It reads the input and executes the game class."
    # Number of players
    num_players = input("Please type the number of players(2-4):")
    while not is_num_in_range(num_players, 2, 4):
        num_players = input("Please type the number of players(2-4):")
    # Number of human players
    num_humans = input("Please type the number of human players(1-" \
                                                + str(num_players) + "):")
    while not is_num_in_range(num_humans, 1, int(num_players)):
        num_humans = input("Please type the number of human players(1-" \
                                                + str(num_players) + "):")
    # Number of pawns per player
    num_pawns = input("Please type the number of pawns per player(1-4):")
    while not is_num_in_range(num_pawns, 1, 4):
        num_pawns = input("Please type the number of pawns per player(1-4):")
    # Number of pawns that need to cross the finish line in order to win.
    num_finish = input("Please type the number of pawns that must cross " \
               + "the finish line in order to win the game(1-" + str(num_pawns) + "):")
    while not is_num_in_range(num_finish, 1, int(num_pawns)):
        num_finish = input("Please type the number of pawns that must cross " \
               + "the finish line in order to win the game(1-" + str(num_pawns) + "):")
    # Executes the game.
    game = Game(num_players, num_humans, num_pawns, num_finish)
    game.position_deep_pits()
    game.position_black_holes()
    game.run()
