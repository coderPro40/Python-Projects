# Name: Franck Dosso
# Partners: Leandro Aguiar, ThankGod Oforum
# Fuction: Create Sound System for game Ludo


import pygame, sys, random, math
from pygame.locals import *
import os

pygame.init()
pygame.mixer.init()
class soundGallery:
    def __init__(self):
        #load all sound effects
        self.suspens = pygame.mixer.Sound(os.path.join('snd', "getin.wav"))
        self.laugh = pygame.mixer.Sound(os.path.join('snd', "Laugh.wav"))
        self.dice = pygame.mixer.Sound(os.path.join('snd', "dice.wav"))
        self.getOut = pygame.mixer.Sound(os.path.join('snd', "applause.wav"))
        self.onePiece = pygame.mixer.Sound(os.path.join('snd', "onePiece.wav"))
        self.finishline = pygame.mixer.Sound(os.path.join('snd', "finishline.wav"))
        self.select = pygame.mixer.Sound(os.path.join('snd', "select.wav"))
        self.pit = pygame.mixer.Sound(os.path.join('snd', "pit.wav"))
        self.blackhole = pygame.mixer.Sound(os.path.join('snd', "sad.wav"))
        self.move = pygame.mixer.Sound(os.path.join('snd', "move.wav"))
        self.dpits = pygame.mixer.Sound(os.path.join('snd', "dpits.wav"))
        self.bholes = pygame.mixer.Sound(os.path.join('snd', "bholes.wav"))
        self.rollit = pygame.mixer.Sound(os.path.join('snd', "rollit.wav"))
        self.nomove = pygame.mixer.Sound(os.path.join('snd', "nomove.wav"))
        self.clickmove = pygame.mixer.Sound(os.path.join('snd', "clickmove.wav"))
        self.one = pygame.mixer.Sound(os.path.join('snd', "one.wav"))
        self.two = pygame.mixer.Sound(os.path.join('snd', "two.wav"))
        self.three = pygame.mixer.Sound(os.path.join('snd', "three.wav"))
        self.four = pygame.mixer.Sound(os.path.join('snd', "four.wav"))
        self.five = pygame.mixer.Sound(os.path.join('snd', "five.wav"))
        self.six = pygame.mixer.Sound(os.path.join('snd', "six.wav"))
        self.won = pygame.mixer.Sound(os.path.join('snd', "won.wav"))
        self.ovation = pygame.mixer.Sound(os.path.join('snd', "ovation.wav"))
        

    # Just an extra sound in case
    #also fadeout attribute is represented in milliseconds
    def play_suspens(self):
        self.suspens.play()
        self.suspens.set_volume(1)
        self.suspens.fadeout(2000)

    #When a player lands on another player's piece  
    def play_laugh(self):
        self.laugh.play()
        self.suspens.set_volume(1)
        self.suspens.fadeout(3000)

    #When the player roll the dice
    def play_dice(self):
        self.dice.play()
        self.suspens.set_volume(1)
        self.suspens.fadeout(3000)
    #When you get out of your homeground
    def get_out(self):
        self.getOut.play()
  
    #When you get one piece accross finish line
    def finish_line(self):
        self.finishline.play()
        self.suspens.set_volume(1)
        self.suspens.fadeout(3000)

    #When you get a piece into finish line area
    def one_piece(self):
        self.onePiece.play()
        self.suspens.set_volume(1)
        self.suspens.fadeout(3000)
    #when player select which die roll to go with
    def play_select(self):
        self.select.play()
        self.suspens.set_volume(1)
        #self.suspens.fadeout(3000)

    #When player lands onto pit
    def pit(self):
        self.pit.play()
        self.suspens.set_volume(1)
        self.suspens.fadeout(3000)

     #When you get into black hole
    def black_hole(self):
        self.blackhole.play()
        self.blackhole.set_volume(1)

    #When you get into black hole
    def play_move(self):
        self.move.play()
        self.move.set_volume(1)
    # Stop sound
    def stop_sound(self):
        pygame.mixer.stop()

    #When you get into black hole
    def say_dpits(self):
        self.dpits.play()
        self.dpits.set_volume(1)

     #When you get into black hole
    def say_bholes(self):
        self.bholes.play()
        self.bholes.set_volume(1)

      #When you get into black hole
    def say_rollit(self):
        self.rollit.play()
        self.rollit.set_volume(1)

      #When you get into black hole
    def click_move(self):
        self.clickmove.play()
        self.clickmove.set_volume(1)

      #When you get into black hole
    def no_move(self):
        self.nomove.play()
        self.nomove.set_volume(1)
       #When you get into black hole
    def say_one(self):
        self.one.play()
        self.one.set_volume(1)

       #When you get into black hole
    def say_two(self):
        self.two.play()
        self.two.set_volume(1)

       #When you get into black hole
    def say_three(self):
        self.three.play()
        self.three.set_volume(1)

       #When you get into black hole
    def say_four(self):
        self.four.play()
        self.four.set_volume(1)
                                            

      #When you get into black hole
    def say_five(self):
        self.five.play()
        self.five.set_volume(1)

      #When you get into black hole
    def say_six(self):
        self.six.play()
        self.six.set_volume(1)

       #When you get into black hole
    def say_won(self):
        self.won.play()
        self.six.set_volume(1)

       #When you get into black hole
    def say_ovation(self):
        self.ovation.play()
        self.six.set_volume(1)




#-----------------------------------------------------------------------PART2-----------------------------------------------------------------------------------------#
class musicGallery:

    def __init__(self):
        self.queue = pygame.mixer.music.get_pos()

    #Music played on intro page
    def load_themesong(self):
         pygame.mixer.music.load(os.path.join('snd', "Juicy.wav"))
    #Music played when player pauses the game
    def load_pausesong(self):
        pygame.mixer.music.load(os.path.join('snd', "pause.wav"))
    #Music played when a victory occurs
    def load_winSong(self):
        pygame.mixer.music.load(os.path.join('snd', "win.wav"))
    # Play loaded music
    def play_song(self, ntimes):
        pygame.mixer.music.play(ntimes)
    # Stop music that's being played
    def stop_music(self):
        pygame.mixer.music.stop()

     # Pause music that's being played
    def pause_music(self):
        pygame.mixer.music.pause()

     # Unpause music that's being played
    def unpause_music(self):
        pygame.mixer.music.unpause()

     # set volume
    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

        



    
