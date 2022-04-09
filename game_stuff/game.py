"""The start of bad-megaman"""

import pygame
from player import Player


pygame.init()

display = pygame.display.set_mode((600, 600))

while True:

    display.fill((123, 175, 212))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    player: Player = Player(200, 200, 128, 128)

    pygame.display.update()