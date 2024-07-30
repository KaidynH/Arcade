import pygame, math
from Enemies.enemy_class import Enemy

class Bumblebee(Enemy):
    def __init__(self, pX, pY, pPath):
        # Initialize parent class
        super().__init__('Galaga\Images\Bumblebee.png', 40, 5, pX, pY, 90)

        # Position along the path
        self.position = 1

        # Bee path
        self.path = pPath
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