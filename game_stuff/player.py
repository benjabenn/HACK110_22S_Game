"""PLAYER STUFF"""
import pygame
from pygame.locals import RLEACCEL

class Player(pygame.sprite.Sprite):
     
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = pygame.image.load("game_stuff/assets/TARHEELMAN.png")
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.image.set_colorkey((50,50,40))

    # def gravity(self):
        # self.movey += 3.2
        # if self.rect.y> >

    # def update(self):
    #     # self.rect.x = self.rect.x + self.movex
    #     # def jump(self):

    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)