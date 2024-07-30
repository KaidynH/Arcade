import pygame, math
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee

pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Galaga')

player = Player()

bullet_list = []


bee = Bumblebee(350, 400, [(100, 200), (300, 400)])

bee.Paths.test()




# while True:
#     screen.fill((0,0,0))

#     for circle in circles:
#         pygame.draw.circle(screen, (255,255,255), (circle), 5)
    

    
#     screen.blit(bee.image, bee.rect.topleft)
#     screen.blit(bee2.image, bee2.rect.topleft)
#     screen.blit(bee3.image, bee3.rect.topleft)
#     screen.blit(bee4.image, bee4.rect.topleft)


#     pygame.display.update()
#     pygame.time.delay(20)