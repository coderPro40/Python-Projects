"""
Name: ThankGod Ofurum, Franck Dosso, Leandro
Function: Create and test game modes with pygame
tools and guis.
"""

import pygame, sys, random, math, string
from pygame.locals import *
from GameSound import *
import pickle
from Ludo import *
import ctypes

#class instances
pygame.mixer.init()
sound = soundGallery()
music = musicGallery()
color = [White, Black, brown, Lbrown, Red, Green, Blue, Gold, Purple, Orange, Yellow] = (255, 255, 255), (0, 0, 0), (218,165,32), (238,221,130) , (0, 255, 0), (255, 0, 0), (0, 0, 255), (218, 165, 32), (160, 32, 240), (255, 165, 0), (255, 255, 0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
FPS = 60
        
#Function for controlling button events and actions
def _button(screen, msg, x, y, w, h, s, action = None, Class = None):# game buttons function
    Menu = GameMenu()#instance of menu class
    Instructions = Instruction()#instance of instruction class
    players = Player()#instance of player class
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + w) > mouse[0] > x and (y + h) > mouse[1] > y:# Hover over button box
        Text = pygame.font.Font("freesansbold.ttf", s+15)#text for box
        if click[0] == 1 and action != None:# execute action on click
            if action == 'New Game':
                sound.play_select()
                players.on_execute()
            elif action == 'Instruction':
                sound.play_select()
                Instructions.on_execute()
            elif action == 'Quit':
                Menu.on_cleanup()
            elif action == 'Back':
                sound.play_select()
                Menu.on_execute()
            elif action == 'Begin':
                # Start the game
                cfg_file = open(os.path.join('cfg', 'game_cfg.txt'), 'r')
                PlayNum = open(os.path.join('cfg', 'playNum.txt'), 'r')
                PieceStart = open(os.path.join('cfg', 'pieceStart.txt'), 'r')
                num_players = PlayNum.read()
                num_pawns = PieceStart.read()
                num_finish = cfg_file.read()
                cfg_file.close()
                PlayNum.close()
                PieceStart.close()
                game = Game(num_players, num_players, num_pawns, num_finish)
                game.position_deep_pits()
                game.position_black_holes()
                game.run()
            
    else:
        Text = pygame.font.Font("freesansbold.ttf", s)#text for box

    textSurf, textRect = _textObject(msg, Text)
    textRect.center = ((x + (w / 2)), (y +(h / 2)))
    screen.blit(textSurf, textRect)

def _textObject(text, font):#create text object in box
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()

class Input:
    "Input for game text"
    def __init__(self, x, y, w, h, s, prompt):
        self.x = x; self.y = y; self.w = w; self.h = h
        self.font = pygame.font.Font("freesansbold.ttf", s)#text for box
        self.maxlength = 1
        self.prompt = prompt; self.value = ''
        self.textOneRect, self.textTwoRect = None, None
        self.pressed = False

    def draw(self, surface):
        """ Draw the text input to a surface """
        textOne = self.font.render(self.prompt, 1, color[1])
        textTwo = self.font.render(self.value, 1, color[1])
        self.textOneRect = textOne.get_rect().center = ((self.x + (self.w / 2)), (self.y +(self.h / 2)))
        self.textTwoRect = textTwo.get_rect().center = (((self.x + (self.w / 2)) + 280), (self.y +(self.h / 2)))
        pygame.draw.rect(surface, color[8], ((self.x + 400), (self.y + 7.5), self.w/3.5, self.h))
        surface.blit(textOne, self.textOneRect)
        surface.blit(textTwo, self.textTwoRect)

    def update(self, events, surface):
        """ Update the input based on passed events """
        for event in events:
            if event.type == MOUSEMOTION:
                a, b = event.pos
                if ((self.x + 400) + (self.w/3.5)) > a > (self.x + 400) and ((self.y + 7.5) + self.h) > b > (self.y + 7.5):
                    pygame.draw.rect(surface, color[10], ((self.x + 400), (self.y + 7.5), self.w/3.5, self.h))
            if event.type == MOUSEBUTTONDOWN:
                a, b = event.pos
                if ((self.x + 400) + (self.w/3.5)) > a > (self.x + 400) and ((self.y + 7.5) + self.h) > b > (self.y + 7.5):
                    sound.play_select()
                    if event.button == 1:
                        self.pressed = True
            if event.type == KEYDOWN and self.pressed == True:
                if event.key == K_BACKSPACE: self.value = self.value[:-1]; self.pressed = False
                elif event.key == K_2: self.value += '2'; self.pressed = False; return str(self.value)
                elif event.key == K_3: self.value += '3'; self.pressed = False; return str(self.value)
                elif event.key == K_4: self.value += '4'; self.pressed = False; return str(self.value)

        if len(self.value) > self.maxlength and self.maxlength >= 0: self.value = self.value[:-1]

class Player:#player menu
    def __init__(self):#game initializations
        self._mainClock = None
        self._running = True
        self._winScreen = None
        self.size = self.width, self.height = width, height
        self.FPS = FPS
        self.color = color
        self.numPlayer = None
        self.numSPiece = None
        self.numFPiece = None

    def on_init(self):#start game initializations
        pygame.init()
        self.numPlayer = Input((60/200)*self.width, (90/200)*self.height, self.width/4.3, self.height/20, 20, 'Number of Players: ')
        self.numSPiece = Input((60/200)*self.width, (106/200)*self.height, self.width/4.3, self.height/20, 20, 'Number of Start Pieces: ')
        self.numFPiece = Input((60/200)*self.width, (129/200)*self.height, self.width/4.3, self.height/20, 20, 'Number of End Pieces: ')
        self._mainClock = pygame.time.Clock()
        self._winScreen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        self._running = True
        self.Play = pygame.image.load(os.path.join('img', 'GameMenu.jpg'))
        self.Play = pygame.transform.scale(self.Play, (self.width, self.height))
        pygame.display.set_caption('Ludo')

    def on_event(self, event):#Event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   self._running = False
            
    def on_loop(self):#Main game loop
        pygame.event.pump()
        self._winScreen.blit(self.Play, (0,0))
        self.numPlayer.draw(self._winScreen)
        self.numSPiece.draw(self._winScreen)
        self.numFPiece.draw(self._winScreen)

    def on_render(self):#Deal with text and messages/ dialogues
        _button(self._winScreen,"Begin", (83/200)*self.width, (147.5/200)*self.height, self.width/4.3, self.height/20, 20, 'Begin')
        pygame.display.update()
        self._mainClock.tick(self.FPS)
        
    def on_cleanup(self):#Turn game off
        pygame.quit()
        sys.exit()
 
    def on_execute(self):#Execute game code
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.on_loop()
            events = pygame.event.get()
            for event in events:
                self.on_event(event)
            NP = self.numPlayer.update(events, self._winScreen)
            NSP = self.numSPiece.update(events, self._winScreen)
            NFP = self.numFPiece.update(events, self._winScreen)
            if (NP != None) and (NP != ''):
                PlayNum = open(os.path.join('cfg', 'playNum.txt'), 'w')
                PlayNum.write(str(NP))
                PlayNum.close()
            if (NSP != None) and (NSP != ''):
                PieceStart = open(os.path.join('cfg', 'pieceStart.txt'), 'w')
                PieceStart.write(str(NSP))
                PieceStart.close()
            if (NFP != None) and (NFP != ''):
                cfg_file = open(os.path.join('cfg', 'game_cfg.txt'), 'w')
                cfg_file.write(str(NFP))
                cfg_file.close()
                
            self.on_render()
        self.on_cleanup()

class Instruction:#instruction menu
    def __init__(self):#game initializations
        self._mainClock = None
        self._running = True
        self._winScreen = None
        self.size = self.width, self.height = width, height
        self.FPS = FPS
        self.color = color

    def on_init(self):#start game initializations
        pygame.init()
        self._mainClock = pygame.time.Clock()
        self._winScreen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        self._running = True
        self.Instruct = pygame.image.load(os.path.join('img', 'ludoInstructions.jpg'))
        self.Instruct = pygame.transform.scale(self.Instruct, (self.width, self.height))
        pygame.display.set_caption('Ludo')

    def on_event(self, event):#Event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   self._running = False
            
    def on_loop(self):#Main game loop
        pygame.event.pump()
        self._winScreen.blit(self.Instruct, (0,0)) 

    def on_render(self):#Deal with text and messages/ dialogues 
        _button(self._winScreen,"Back", (19/200)*self.width, (181.5/200)*self.height, self.width/4.3, self.height/20, 30, 'Back')
        pygame.display.update()
        self._mainClock.tick(self.FPS)
        
    def on_cleanup(self):#Turn game off
        pygame.quit()
        sys.exit()
 
    def on_execute(self):#Execute game code
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.on_loop()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

class GameMenu:#Main menu
    def __init__(self):#game initializations
        self._mainClock = None
        self._running = True
        self._winScreen = None
        self.size = self.width, self.height = width, height
        self.color = color
        self.FPS = FPS
        self.Menu = None

    def on_init(self):#start game initializations
        pygame.init()
        self._mainClock = pygame.time.Clock()
        self._winScreen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.FULLSCREEN)
        self._running = True
        self.Menu = pygame.image.load(os.path.join('img', 'GameMenu.jpg'))
        self.Menu = pygame.transform.scale(self.Menu, (self.width, self.height))
        pygame.display.set_caption('Ludo')

    def on_event(self, event):#Event handler
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == KEYDOWN:
               if event.key == K_ESCAPE:
                   self._running = False
            
    def on_loop(self):#Main game loop
        pygame.event.pump()
        self._winScreen.blit(self.Menu, (0,0))
            
    def on_render(self):#Deal with text and messages/ dialogues
        _button(self._winScreen,"New Game", (83/200)*self.width, (92/200)*self.height, self.width/4.3, self.height/20, 20, 'New Game')
        _button(self._winScreen,"Load Game", (83/200)*self.width, (108.5/200)*self.height, self.width/4.3, self.height/20, 20, 'Load Game')
        _button(self._winScreen,"Instruction", (83/200)*self.width, (131.5/200)*self.height, self.width/4.3, self.height/20, 20, 'Instruction')
        _button(self._winScreen,"Quit", (83/200)*self.width, (147.5/200)*self.height, self.width/4.3, self.height/20, 20, 'Quit')
        pygame.display.update()
        self._mainClock.tick(self.FPS)
        
    def on_cleanup(self):#Turn game off
        pygame.quit()
        sys.exit()
 
    def on_execute(self):#Execute game code
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            self.on_loop()
            for event in pygame.event.get():
                self.on_event(event)
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :#Run game 
    GameMenu().on_execute()
    
