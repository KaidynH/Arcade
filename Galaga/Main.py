import pygame
import numpy as np
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee
from Curves import bezier_curve

pygame.init()
screen = pygame.display.set_mode((700, 800), pygame.DOUBLEBUF)
pygame.display.set_caption('Galaga')

player = Player()


bees = [Bumblebee(275, -50, 'l', 0), Bumblebee(275, -100, 'l', 1), Bumblebee(275, -150, 'l', 2), Bumblebee(275, -200, 'l', 3),
        Bumblebee(425, -50, 'r', 0), Bumblebee(425, -100, 'r', 1), Bumblebee(425, -150, 'r', 2), Bumblebee(425, -200, 'r', 3)]

# bees = [Bumblebee(274, -50, np.array([[266, 67], [250, 74], [348, 1000], [498, 247]]))]


bullet_list = []

running = True
while running:
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            # Add a bullet to the bullet list everytime space is pressed
            if event.key == pygame.K_SPACE:
                bullet_list.append(Bullet(player.x + 20, player.y))

    # Bullet actions
    for bullet in bullet_list[:]:
        bullet.action(screen)

        # Remvoe the bullet once it is off the screen
        if bullet.y < -15:
            bullet_list.remove(bullet)

    # Player actions
    player.action(screen)

    # Enemy actions
    for bee in bees:
        bee.action(screen)
    


    
    pygame.display.update()
    pygame.time.delay(5)

pygame.quit()