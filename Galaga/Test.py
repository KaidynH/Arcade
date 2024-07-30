import pygame, math
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee

pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Galaga')

player = Player()

bullet_list = []


bee = Bumblebee(350, 400)

bee2 = Bumblebee(200, 200)

bee3 = Bumblebee(500, 300)

bee4 = Bumblebee(100, 700)

print(bee.angles)
print(bee.angle)
# bee.image = bee.rotate(0)
bee.image = bee.rotate(bee.angles[0]-bee.angle)
print(bee.angle)
bee2.image = bee2.rotate(bee.angles[1]-bee.angle)
# bee2.image = bee2.rotate(45)
print(bee2.angle)
bee3.image = bee3.rotate(bee.angles[2]-bee.angle)
print(bee3.angle)
# bee4.image = bee4.rotate(270)

circles = [(350, 400), (200, 200), (500, 300), (100,700), (0,0)]




# print(math.degrees(math.atan2(200,-150))+90)
# print(math.degrees(math.atan2(-100,300))+90)
# print(math.degrees(math.atan2(-400,-400))+90)
# print(math.degrees(math.atan2(300,250))+90)





while True:
    screen.fill((0,0,0))

    for circle in circles:
        pygame.draw.circle(screen, (255,255,255), (circle), 5)
    

    
    screen.blit(bee.image, bee.rect.topleft)
    screen.blit(bee2.image, bee2.rect.topleft)
    screen.blit(bee3.image, bee3.rect.topleft)
    screen.blit(bee4.image, bee4.rect.topleft)


    pygame.display.update()
    pygame.time.delay(20)