import pygame
import random

class Falling(pygame.sprite.Sprite):
    x: int
    y: int

    def __init__(self) -> None:
        super().__init__()
        self.x = (random.randint(80, 600))
        self.y = 0
        self.image = pygame.image.load("game_stuff/assets/Duke_Enemy.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()     
    def fall(self):
        self.rect.x = random.randint(0, 600)
        self.rect.y += 30
    
    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
        