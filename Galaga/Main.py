import pygame
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee

pygame.init()
screen = pygame.display.set_mode((700, 800), pygame.DOUBLEBUF)
pygame.display.set_caption('Galaga')

player = Player()
bees = [Bumblebee(350, 400, [(350, 400), (200, 200), (500, 300), (100,700), (300, 300), (400,500), (600,600), (500,400)]), Bumblebee(700, 100, [(700, 100), (200, 100), (400, 500), (200, 600), (700, 100), (200, 100), (400, 500), (200, 600), (700, 100), (200, 100), (400, 500), (200, 600), (700, 100), (200, 100), (400, 500), (200, 600), (700, 100), (200, 100), (400, 500), (200, 600)])]

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
    for bee in bees:
        bee.action(screen)


    pygame.display.update()
    pygame.time.delay(5)