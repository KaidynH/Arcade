import pygame, math

class Enemy():
    def __init__(self, pImage, pSize, pSpeed, pX, pY, pAngle):
        # Size of the enemy
        self.width = pSize

        # Speed of the enemy
        self.speed = pSpeed

        # Coordinates of the center of the enemy
        self.x = pX
        self.y = pY

        # Direction the enemy is facing, right is zero degrees
        self.angle = pAngle

        # Path to the image file location
        self.image_path = pImage

        self.render_image()
    
    # Render new image to replace images that become blurry
    def render_image(self):
        # Enemy image variable
        self.image = pygame.image.load(self.image_path).convert_alpha()

        # Transformation variables, aspect ratio mainted to prevent distortion
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        self.height = int(self.width / aspect_ratio)

        # Image size transformation
        self.image = pygame.transform.smoothscale(self.image, (self.width,self.height))

        # Image rectangle
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # Update angle variable
        self.angle = 90





    # Update the coordinate variables
    def update_coordinates(self):
        self.x = self.rect.centerx
        self.y = self.rect.centery
    
    # Rotate to a certain angle with zero degrees to the right
    def rotate(self, angle):
        # Update the current angle
        self.angle = (self.angle + angle) % 360

        # Rotate the image
        rotated_image = pygame.transform.rotate(self.image, angle)

        # Get the new rect and keep the center position the same
        self.rect = rotated_image.get_rect(center=self.rect.center)
        return rotated_image
    
    # Move bee to specific coordinates
    def move(self, position):
        # Slope variables from current to desired position
        run = position[0] - self.x
        rise = position[1] - self.y

        # Slow bee to designated speed
        while math.hypot(self.x - (self.x + run), self.y - (self.y + rise)) > self.speed:
            run /= 1.5
            rise /= 1.5

        # Move the enemy
        self.rect.centerx = self.x + run
        self.rect.centery = self.y + rise

        # Update coordinate variables
        self.update_coordinates()