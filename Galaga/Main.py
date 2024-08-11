import pygame
import numpy as np
from player_class import Player
from bullet_class import Bullet
from Enemies.goei_class import Goei
from Enemies.zako_class import Zako

pygame.init()
screen = pygame.display.set_mode((700, 800), pygame.DOUBLEBUF)
pygame.display.set_caption('Galaga')


def all_in_formation(enemies):
    check = True
    for enemy in enemies:
        if not enemy.in_formation:
            check = False
    
    return check



player = Player()


# bees = [Zako('l', 0, 0), Zako('l', 1, 1), Zako('l', 2, 2), Zako('l', 3, 3), ]
        # Zako('l', 4, 8), Zako('l', 5, 9), Zako('l', 6, 10), Zako('l', 7, 11),
        # Zako('l', 8, 16), Zako('l', 9, 17), Zako('l', 10, 18), Zako('l', 11, 19),
        # Zako('r', 0, 4), Zako('r', 1, 5), Zako('r', 2, 6), Zako('r', 3, 7), 
        # Zako('r', 4, 12), Zako('r', 5, 13), Zako('r', 6, 14), Zako('r', 7, 15), 
        # Zako('r', 8, 20), Zako('r', 9, 21), Zako('r', 10, 22), Zako('r', 11, 23)
       # ]

# butterflies = [Goei('l', 0, 0), Goei('l', 1, 1), Goei('l', 2, 2), Goei('l', 3, 3), 
#         Goei('l', 4, 8), Goei('l', 5, 9), Goei('l', 6, 10), Goei('l', 7, 11),
#         Goei('l', 8, 16), Goei('l', 9, 17), Goei('l', 10, 18), Goei('l', 11, 19),
#         Goei('r', 0, 4), Goei('r', 1, 5), Goei('r', 2, 6), Goei('r', 3, 7), 
#         Goei('r', 4, 12), Goei('r', 5, 13), Goei('r', 6, 14), Goei('r', 7, 15), 
#         Goei('r', 8, 20), Goei('r', 9, 21), Goei('r', 10, 22), Goei('r', 11, 23)
#         ]

attack0 = [Zako('l', 0, 0), Zako('l', 1, 1), Zako('l', 2, 2), Zako('l', 3, 3)]

attack1 = [Zako('r', 0, 4), Zako('r', 1, 5), Zako('r', 2, 6), Zako('r', 3, 7)] #, Zako('r', 4, 8), Zako('r', 5, 9), Zako('r', 6, 10), Zako('r', 7, 11), Zako('r', 8, 12), Zako('r', 9, 13), Zako('r', 10, 14), Zako('r', 11, 15),])

attack2 = [Goei('l', 0, 0), Goei('l', 1, 1), Goei('l', 2, 2), Goei('l', 3, 3)]

attack3 = [Goei('r', 0, 4), Goei('r', 1, 5), Goei('r', 2, 6), Goei('r', 3, 7)]

wave = [attack0, attack1, attack2, attack3]

enemies_os = attack0

wave_pos = 1

bullets = []

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
                bullets.append(Bullet(player.x + 20, player.y))

    # Bullet actions
    for bullet in bullets[:]:
        bullet.action(screen)

        # Remvoe the bullet once it is off the screen
        if bullet.y < -15:
            bullets.remove(bullet)

    # Player actions
    player.action(screen)

    # Enemy actions
    # If the current attack is finished, start the next one
    if all_in_formation(enemies_os) and wave_pos < len(wave):
        enemies_os = np.hstack((np.array(enemies_os), np.array(wave[wave_pos]))).tolist()
        wave_pos += 1
    
    # EIA - Enemies In Action
    eia = [enemy for enemy in enemies_os if not enemy.in_formation]
    for enemy in eia:
        enemy.action(enemy)
    

    for enemy in enemies_os: 
        enemy.check_collision(bullets, enemies_os)
        screen.blit(enemy.image, enemy.rect.topleft)


    for bullet in bullets:
        screen.blit(bullet.image, (bullet.x, bullet.y))
    
    screen.blit(player.image, (player.x, player.y)) 

    
    pygame.display.update()
    pygame.time.delay(5)

pygame.quit()