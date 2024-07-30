import pygame, math
from player_class import Player
from bullet_class import Bullet
from Enemies.bumblebee_class import Bumblebee

pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption('Galaga')

player = Player()

bullet_list = []


# positions = [(57 + (i * 45), 200) for i in range (1, 13)]

# print(positions)

# bee = Bumblebee('l', 0, 0)

# print(f"bee: {bee.formations}")
# print(bee.formation_indexes[0])
# print(bee.formations[0][6])
# print(bee.formaion)


bees = [Bumblebee('l', 0, 0), Bumblebee('l', 1, 1), Bumblebee('l', 2, 2), Bumblebee('l', 3, 3),
        Bumblebee('r', 0, 4), Bumblebee('r', 1, 5), Bumblebee('r', 2, 6), Bumblebee('r', 3, 7)]

colors = [(255,255,255), (255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255), (100,100,100)]

for bee in bees:
    pygame.draw.circle(screen, colors[bees.index(bee)], bee.formaion, 15)

while True:

    screen.fill((0,0,0))

    for bee in bees:
        pygame.draw.circle(screen, colors[bees.index(bee)], bee.formaion, 15)



    pygame.display.update()
    pygame.time.delay(5)