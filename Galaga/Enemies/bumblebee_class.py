import pygame, math
from Enemies.enemy_class import Enemy

class Bumblebee(Enemy):
    def __init__(self):
        # Initialize parent class
        super().__init__('Galaga\Images\Bumblebee.png', 30, 5, 350, 400, 90)

        # Position along the path
        self.position = 0

        # Bee path
        self.path = [(350, 400), (200, 200), (600,500), (100,700)]
        # Directions the bee will face along its path
        self.angles = [round(math.degrees(math.atan2(self.path[i][0] - self.path[i-1][0], self.path[i][1] - self.path[i-1][1]))) for i in range(1, len(self.path))]

        for i in range(len(self.angles)):
            if self.angles[i] < 0:
                self.angles[i] = self.angles[i] + 360

        # Path variables for readability
        self.update_vars()
    
    
    # Update coordinate and distance variables
    def update_vars(self):
        self.adj = self.path[self.position][0] - self.x
        self.opp = self.path[self.position][1] - self.y
        self.path_distance = (self.opp**2 + self.adj**2)**(1/2)

    
    # Display actions
    def action(self, screen):

        # Turn the bee towards the direction it's moving if needed 
        if self.position < len(self.angles):
            angle_difference = self.angles[self.position] - self.angle
            if abs(angle_difference) >= 30:
                angle_change = 25 if angle_difference > 0 else -25
                self.image = self.rotate(angle_change)
                self.angle += angle_change
                print('yes', self.angle, self.angles[self.position], angle_difference)
            elif abs(angle_difference) < 30 and abs(angle_difference) >= 10:
                angle_change = 5 if angle_difference > 0 else -5
                self.image = self.rotate(angle_change)
                self.angle += angle_change
                print('mid', self.angle, self.angles[self.position], angle_difference)
            elif abs(angle_difference) > 5 and abs(angle_difference) < 10:
                self.image = self.rotate(angle_difference/2)
                self.angle += angle_difference/2
                print('no', self.angle, self.angles[self.position], angle_difference)

        # Move the bee along its path
        if self.path_distance > 0:
            self.move(self.path[self.position])
        elif self.position < len(self.path) - 1:
            self.position += 1

        # Update path variables
        self.update_vars()
    
        # Draw the bee to the screen
        screen.blit(self.image, (self.rect.topleft))