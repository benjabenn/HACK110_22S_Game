import pygame

class Background():
    x: int
    y: int
    image: pygame.surface.Surface

    def __init__(self, x = 0, y = 0):
        self.image = pygame.image.load("game_stuff/assets/court.jpg")
    
    def draw(self, display, x = 0, y = 0):
        display.blit(self.image, (x, y))