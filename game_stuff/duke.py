import pygame
import random

class Falling(pygame.sprite.Sprite):
    x: int
    y: int

    def __init__(self, image_path: str) -> None:
        super().__init__()
        self.x = (random.randint(80, 600))
        self.y = 0
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect() 
    
    def fall(self, x: int, y: int):
        self.rect.move_ip(x, y)
        if self.rect.top >= 600:
            self.rect.x = random.randint(0, 600)
            self.rect.y = random.randint(-100, 0)

    def go_up(self, x: int, y: int):
        self.rect.move_ip(x, y)
        if self.rect.top <= 0:
            self.rect.x = random.randint(0, 600)
            self.rect.y = random.randint(600, 700)
    
    def draw(self, screen) -> None:
        screen.blit(self.image, self.rect)
        