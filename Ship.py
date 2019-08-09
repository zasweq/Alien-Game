import pygame
from pygame.sprite import *

#x, y

class Ship(Sprite):

    def __init__(self, gameDisplay):
        super().__init__()
        self.shipImage = pygame.image.load('player.bmp')
        self.shipImage = pygame.transform.scale(self.shipImage, (100, 100))
        self.gameDisplay = gameDisplay;
        self.speed = 20;
        self.mask = pygame.mask.from_surface(self.shipImage)
        self.rect = self.shipImage.get_rect()

        self.screenRect = self.gameDisplay.get_rect()
        self.x = self.screenRect.centerx
        self.y = 700 #HARDCODE THIS, CHANGE LATER MAYBE
        self.rect.left = self.x
        self.rect.right = self.x + 100
        self.rect.top = self.y
        self.rect.bottom = self.y + 100

    def updateShip(self):
        self.gameDisplay.blit(self.shipImage, (self.x, self.y))
        self.rect.left = self.x
        self.rect.right = self.x + 100