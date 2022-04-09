"""The start of bad-megaman"""


import pygame
import sys
from background import Background
from player import Player


pygame.init()

display = pygame.display.set_mode((600, 600))
player = Player(200, 200, 128, 128)

while True:

    display.fill((123, 175, 212))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                player.rect.move_ip(-10, 0)
            elif i.key == pygame.K_RIGHT:
                player.rect.move_ip(10, 0)
            elif i.key == pygame.K_UP:
                player.rect.move_ip(0, -10)
            elif i.key == pygame.K_DOWN:
                player.rect.move_ip(0, 10)
    
    background: Background = Background()

    background.draw(display)

    player.draw(display)

    pygame.display.update()