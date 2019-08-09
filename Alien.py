import pygame
import random
from pygame.sprite import Sprite

#width and height are 100
#w, h = pygame.display.get_surface().get_size()
#random.randrange(0, display_width)
class Alien(Sprite):

    def __init__(self, gameDisplay, randomAI): #Add field 1-4 that will determine how alien updates, one will follow you around, one will go side to side, also can play with amount of bullets on screen
        super().__init__()
        self.alienImage = pygame.image.load('alien.bmp')
        self.alienImage = pygame.transform.scale(self.alienImage, (100, 100))
        self.mask = pygame.mask.from_surface(self.alienImage)
        self.rect = self.alienImage.get_rect()

        self.gameDisplay = gameDisplay
        self.x = random.randrange(0, gameDisplay.get_width()-100)
        self.y = -50 #EXPIREMENT WITH THIS
        #BLIT IS UPPER LEFT
        self.rect.left = self.x
        self.rect.right = self.x + 100
        self.rect.top = self.y
        self.rect.bottom = self.y + 100

        #Simply a random AI
        self.randomAI = randomAI
        self.goingRight = True

    def update(self):
        self.handleXY()
        self.gameDisplay.blit(self.alienImage, (self.x, self.y))
        self.rect.left = self.x
        self.rect.right = self.x + 100
        self.rect.top = self.y
        self.rect.bottom = self.y + 100

    def handleXY(self):
        if self.randomAI == 1:
            self.y += 14
            return
        if self.randomAI == 2: #Back and forth
            if self.x + 50 > self.gameDisplay.get_width():
                self.y += 50
                self.x -= 14
                self.goingRight = False
            if self.x < 0:
                self.y += 50
                self.x += 14
                self.goingRight = True
            if self.goingRight:
                self.x += 14
            else:
                self.x -= 14
        if self.randomAI == 3: #Diagonal
            if self.x + 50 > self.gameDisplay.get_width():
                self.y += 50
                self.x -= 14
                self.goingRight = False
            if self.x < 0:
                self.y += 50
                self.x += 14
                self.goingRight = True
            if self.goingRight:
                self.x += 14
                self.y += 10
            else:
                self.x -= 14
                self.y += 10
        if self.randomAI == 4: #Mayve add later
            pass