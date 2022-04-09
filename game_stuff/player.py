"""PLAYER STUFF"""
import pygame
from pygame.locals import RLEACCEL

class Player(pygame.sprite.Sprite):
     
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ninja.bmp")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0,0,0), RLEACCEL)


    def update(self):
        pressed_keys = pygame.key.get_pressed()
