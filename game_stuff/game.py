"""The start of bad-megaman"""


from matplotlib.pyplot import pause
import pygame
import sys
from background import Background
from player import Player
from duke import Falling
from random import randint


pygame.init()

display = pygame.display.set_mode((600, 600))
player = Player(400, 400, 328, 328)
enemy_1 = Falling("game_stuff/assets/Duke_Enemy.png")
enemy_2 = Falling("game_stuff/assets/ncstate100.png")
enemy_3 = Falling("game_stuff/assets/demon_deacon.png")

pygame.mixer.music.load("game_stuff/assets/caasss.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)

while True:
    display.fill((123, 175, 212))
    speed: int = 25
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                player.rect.move_ip(-speed, 0)
            elif i.key == pygame.K_RIGHT:
                player.rect.move_ip(speed, 0)
            elif i.key == pygame.K_UP:
                player.rect.move_ip(0, -speed)
            elif i.key == pygame.K_DOWN:
                player.rect.move_ip(0, speed)
    

    hit = enemy_1.rect.colliderect(player) or enemy_2.rect.colliderect(player) or enemy_3.rect.colliderect(player)

    if(hit):
        pygame.mixer.music.load("game_stuff/assets/nooo.wav")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)
        print("GAME OVER!")
        pause(5)
        pygame.quit()
        sys.exit()

    background: Background = Background()

    background.draw(display)

    player.draw(display)

    enemy_1.draw(display)
    enemy_1.fall(1, 1)

    enemy_2.draw(display)
    enemy_2.go_up(0, -2)

    enemy_3.draw(display)
    enemy_3.fall(0, 1)

    pygame.display.update()