import pygame
from pygame.sprite import Sprite

class ShipBullet(Sprite):
    def __init__(self, screen, ship):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        #Initial area of bullet
        self.rect.centerx = ship.x + 50
        self.rect.top = ship.y

        self.y = float(self.rect.y)

        self.bulletSpeed = 30 #Expierement with this, everything is discrete right now, maybe I can lower update time

    def update(self):
        #Move bullet upward
        self.y -= self.bulletSpeed
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)