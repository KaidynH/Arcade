import pygame, math
import numpy as np
from Enemies.enemy_class import Enemy

class Zako(Enemy):
    def __init__(self, pEntry, pPos, pFormation):
        # Initial Coordinates
        x = 425 if pEntry == 'r' else 275
        y = -50 - (50 * pPos)

        # Initialize parent class
        super().__init__('Galaga\Images\Zako.png', 30, 5, x, y, 90)

        # Zako position indexes related to the formation parameter
        self.formation_indexes = np.array([ [0, 5], [0, 6], [1, 5], [1, 6], [0, 4], [0, 7], [1, 4], [1, 7], [0, 3], [0, 8], [1, 3], [1, 8], [0, 2], [0, 9], [1, 2], [1, 9], [0, 1], [0, 10], [1, 1], [1, 10], [0, 0], [0, 11], [1, 0], [1, 11] ])

        # Zako formation positions
        self.formations = np.array([[[57 + (i * 45), 250] for i in range (1, 13)], [[57 + (i * 45), 300] for i in range (1, 13)]])

        # Zako position in formation
        self.formation = self.formations[self.formation_indexes[pFormation][0]][self.formation_indexes[pFormation][1]]

        # Position along the path
        self.position = 1
        
        # Zako path
        self.path = self.Paths.r_entry() if pEntry == 'r' else self.Paths.l_entry()
        self.path = np.vstack((self.path, self.Paths.formation_entry(self)))

        # Directions the zako will face along its path
        self.angles = []
        for i in range(1,len(self.path)):
            angle = round(math.degrees(math.atan2(-(self.path[i][1]-self.path[i-1][1]), (self.path[i][0]-self.path[i-1][0]))))
            self.angles.append(angle)
        
        for angle in self.angles:
            if angle < 0:
                self.angles[self.angles.index(angle)] = angle + 360


