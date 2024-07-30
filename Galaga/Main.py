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

P0 = np.array([274, -26])
P1 = np.array([1000, 150])
P2 = np.array([-900, 550])
P3 = np.array([600, 700])

control_points = np.array([P0, P1, P2, P3])


bees = [Bumblebee(274, -50, bezier_curve.draw_line(control_points))]

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

pygame.QUIT()