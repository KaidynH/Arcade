import pygame
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee

pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Galaga')

player = Player()

bullet_list = []


bee = Bumblebee()

x, y = 350, 400

while True:
    screen.fill((0,0,0))

    bee.action(screen)
    bee.image = bee.rotate(45)

    pygame.display.update()
    pygame.time.delay(500)