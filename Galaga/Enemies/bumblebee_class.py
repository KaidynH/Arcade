import pygame, math
from Enemies.enemy_class import Enemy

class Bumblebee(Enemy):
    def __init__(self):
        # Initialize parent class
        super().__init__('Galaga\Images\Bumblebee.png', 30, 5, 350, 400, 90)

        # Bee path
        self.path = [(200, 200), (600,500)]

        # Position along the path
        self.position = 0

        # Path variables for readability
        self.update_vars()
    
    
    # Update coordinate and distance variables
    def update_vars(self):
        self.opp = self.path[self.position][0] - self.x
        self.adj = self.path[self.position][1] - self.y
        self.path_distance = (self.opp**2 + self.adj**2)**(1/2)
        self.path_angle = math.degrees(math.atan2(self.opp, self.adj))
        print(self.path_angle - self.angle)

    
    # Display actions
    def action(self, screen):
        # Turn the bee towards the direction it's moving
        if abs(self.angle - self.path_angle) > 5:
            self.image = self.rotate(5)
            self.angle += self.path_angle - self.angle

        # Move the bee along its path
        if self.path_distance > 0:
            self.move(self.path[self.position])
        elif self.position < len(self.path) - 1:
            self.position += 1

        # Update path variables
        self.update_vars()
    
        # Draw the bee to the screen
        screen.blit(self.image, (self.rect.topleft))