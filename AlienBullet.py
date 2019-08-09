import pygame
from pygame.sprite import Sprite

class AlienBullet(Sprite):
    def __init__(self, screen, alien):
        super().__init__()

        self.screen = screen
        self.image = pygame.image.load('bullet.bmp')
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.centerx = alien.x + 50
        self.rect.top = alien.y + 100

        self.y = float(self.rect.y)

        self.bulletSpeed = 30 #Expierement with this

    def update(self):
        #Move bullet downward
        self.y += self.bulletSpeed
        self.rect.y = self.y
        self.screen.blit(self.image, self.rect)
