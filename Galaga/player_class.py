import pygame

class Player:
    def __init__(self):
        # Size of the ship
        self.size = 40

        # Speed of the ship
        self.speed = 2

        # Coordinates of the top left of the ship
        self.x = 250
        self.y = 720

        # Ship image variable
        self.image = pygame.image.load('Galaga\Images\Ship.png')

        # Image size transformation
        self.image = pygame.transform.scale(self.image, (self.size,self.size))

    
    # Move the ship left or right
    def move(self, direction):
        if direction == 'right' and self.x < 650:
            self.x += self.speed

        if direction == 'left' and self.x > 0:
            self.x -= self.speed
    
    # Player action method
    def action(self, screen):
        keys = pygame.key.get_pressed()

        # Move right when right arrow key pressed
        if keys[pygame.K_RIGHT]:
            self.move('right')
        
        # Move left when left arrow key pressed
        if keys[pygame.K_LEFT]:
            self.move('left')
        
        # Draw the ship to the screen
        screen.blit(self.image, (self.x, self.y))

        


        
