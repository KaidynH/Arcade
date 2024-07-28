import pygame
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee

pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Galaga')

player = Player()

bee = Bumblebee()

bullet_list = []

while True:
    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()


    for event in pygame.event.get():
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
    bee.action(screen)


    pygame.display.update()
    pygame.time.delay(20)