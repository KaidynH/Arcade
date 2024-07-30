import pygame, math
import numpy as np
from Enemies.enemy_class import Enemy
from Curves import bezier_curve

class Bumblebee(Enemy):
    def __init__(self, pEntry, pPos, pFormation):
        # Initial Coordinates
        x = 425 if pEntry == 'r' else 275
        y = -50 - (50 * pPos)

        # Initialize parent class
        super().__init__('Galaga\Images\Bumblebee.png', 30, 5, x, y, 90)

        # Bee position indexes related to the formation parameter
        self.formation_indexes = np.array([ [0, 5], [0, 6], [1, 5], [1, 6], [0, 4], [0, 7], [1, 4], [1, 7], [0, 3], [0, 8], [1, 3], [1, 8], [0, 2], [0, 9], [1, 2], [1, 9], [0, 1], [0, 10], [1, 1], [1, 10], [0, 0], [0, 11], [1, 0], [1, 11] ])

        # Bee formation positions
        self.formations = np.array([[[57 + (i * 45), 200] for i in range (1, 13)], [[57 + (i * 45), 250] for i in range (1, 13)]])

        # Bee position in formation
        self.formaion = self.formations[self.formation_indexes[pFormation][0]][self.formation_indexes[pFormation][1]]


        # Position along the path
        self.position = 1

        # Bee path
        self.path = self.Paths.r_entry() if pEntry == 'r' else self.Paths.l_entry()
        self.path = self.path[:(-(pPos*3))-1]

        # Directions the bee will face along its path
        self.angles = []
        for i in range(1,len(self.path)):
            angle = round(math.degrees(math.atan2(-(self.path[i][1]-self.path[i-1][1]), (self.path[i][0]-self.path[i-1][0]))))
            self.angles.append(angle)
        
        for angle in self.angles:
            if angle < 0:
                self.angles[self.angles.index(angle)] = angle + 360

        # Path variables for readability
        self.update_vars()
    
    
    # Update coordinate and distance variables
    def update_vars(self):
        self.adj = self.path[self.position][0] - self.x
        self.opp = self.path[self.position][1] - self.y
        self.path_distance = (self.opp**2 + self.adj**2)**(1/2)

    
    # Display actions
    def action(self, screen):

        # Render new image to prevent distortion
        if self.position % 2 == 0:
            self.render_image()
        
        # Turn the bee towards the direction it's moving if needed 
        if abs(self.angle - self.angles[self.position-1]) > 5:
            self.image = self.rotate(self.angles[self.position-1] - self.angle)

        # Move the bee along its path
        if self.path_distance > 0:
            self.move(self.path[self.position])
        elif self.position < len(self.path) - 1:
            self.position += 1

        # Update path variables
        self.update_vars()
    
        # Draw the bee to the screen
        screen.blit(self.image, (self.rect.topleft))
    

    
    # Bee Movement Paths
    class Paths():
        def r_entry():
            # First path
            P00 = np.array([425, -20])
            P01 = np.array([375, 120])
            P02 = np.array([325, 190])
            P03 = np.array([125, 300])

            control_points_1 = np.array([P00, P01, P02, P03])

            path_1 = bezier_curve.draw_line(control_points_1)

            # Second path
            P10 = np.array([125, 300])
            P11 = np.array([-100, 430])
            P12 = np.array([95, 645])
            P13 = np.array([290, 400])

            control_points_2 = np.array([P10, P11, P12, P13])

            path_2 = bezier_curve.draw_line(control_points_2)

            final_path = np.vstack((path_1, path_2))

            return final_path
    
        def l_entry():
            # First path
            P00 = np.array([275, -20])
            P01 = np.array([325, 120])
            P02 = np.array([375, 190])
            P03 = np.array([575, 300])

            control_points_1 = np.array([P00, P01, P02, P03])

            path_1 = bezier_curve.draw_line(control_points_1)

            # Second path
            P10 = np.array([575, 300])
            P11 = np.array([800, 430])
            P12 = np.array([605, 645])
            P13 = np.array([410, 400])

            control_points_2 = np.array([P10, P11, P12, P13])

            path_2 = bezier_curve.draw_line(control_points_2)

            final_path = np.vstack((path_1, path_2))

            return final_path