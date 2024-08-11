import pygame

class Bullet:
    def __init__(self, x, y):
        
        # Size of the bullet hit box
        self.size = 7

        # Speed the bullet moves
        self.speed = 5

        # Coordinates of the top left of the bullet
        self.x = x
        self.y = y

        # Ship image variable
        self.image = pygame.image.load('Galaga\Images\Bullet.png')

        # Image size transformation
        self.image = pygame.transform.scale(self.image, (10,15))
    
    # Bullet action method
    def action(self, screen):
        # Move the bullet up the screen
        self.y -= self.speed
