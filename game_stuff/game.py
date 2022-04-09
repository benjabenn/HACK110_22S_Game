"""The start of bad-megaman"""

import pygame

pygame.init()

display = pygame.display.set_mode((600, 600))

while True:

    display.fill((123, 175, 212))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    

    pygame.display.update()