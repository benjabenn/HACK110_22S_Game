import pygame


class Background():
    x: int
    y: int
    image: pygame.surface.Surface

    def __init__(self, x = 0, y = 0):
        self.image = self.image.load("game_stuff/assets/magma.png")
    
    def draw(self, display, x, y):
        display.blit(self.image, (x, y))

        