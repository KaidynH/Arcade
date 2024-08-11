import pygame, math
import numpy as np
from Curves import bezier_curve

class Enemy():
    def __init__(self, pImage, pSize, pSpeed, pX, pY, pAngle):
        # Width of the enemy
        self.width = pSize

        self.size = self.width // 2

        # Speed of the enemy
        self.speed = pSpeed

        # Coordinates of the center of the enemy
        self.x = pX
        self.y = pY

        # Direction the enemy is facing, right is zero degrees
        self.angle = pAngle

        # Path to the image file location
        self.image_path = pImage

        # Tracks when the enemy is in formation
        self.in_formation = False

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
    
    # Move enemy to specific coordinates
    def move(self, position):
        # Slope variables from current to desired position
        run = position[0] - self.x
        rise = position[1] - self.y

        # Slow enemy to designated speed
        while math.hypot(self.x - (self.x + run), self.y - (self.y + rise)) > self.speed:
            run /= 1.5
            rise /= 1.5

        # Move the enemy
        self.rect.centerx = self.x + run
        self.rect.centery = self.y + rise

        # Update coordinate variables
        self.update_coordinates()
    

    # Check to see if the enemy has been hit by a bullet
    def check_collision(self, bullet_list, enemy_list):
        point_1 = np.array([self.x, self.y])
        for bullet in bullet_list[:]:
            point_2 = np.array([bullet.x, bullet.y])
            if np.linalg.norm(point_1 - point_2) < (self.size + bullet.size):
                enemy_list.remove(self)
                bullet_list.remove(bullet)

    

    # Display actions
    def action(self, enemy):

        # Render new image to prevent distortion
        if self.position % 2 == 0:
            self.render_image()
        
        # Turn the bee towards the direction it's moving if needed 
        if self.angle != self.angles[self.position-1]:
            self.image = self.rotate(self.angles[self.position-1] - self.angle)

        # Move the bee along its path
        path_distance = np.linalg.norm(np.array([self.x, self.y]) - np.array([self.path[self.position][0], self.path[self.position][1]]))
        if path_distance > 0:
            self.move(self.path[self.position])
        elif self.position < len(self.path) - 1:
            self.position += 1

        self.in_formation = True if np.array_equal(np.array([self.x, self.y]), enemy.formation) else False
    


    class Paths():
        def r_entry():
            # First path
            P00 = np.array([425, -20])
            P01 = np.array([375, 120])
            P02 = np.array([325, 190])
            P03 = np.array([125, 300])

            control_points_1 = np.array([P00, P01, P02, P03])

            path_1 = bezier_curve.draw_line(control_points_1, 10)

            # Second path
            P10 = np.array([125, 300])
            P11 = np.array([-100, 430])
            P12 = np.array([150, 700])
            P13 = np.array([310, 450])

            control_points_2 = np.array([P10, P11, P12, P13])

            path_2 = bezier_curve.draw_line(control_points_2, 25)

            final_path = np.vstack((path_1, path_2))

            return final_path
    
        def l_entry():
            # First path
            P00 = np.array([275, -20])
            P01 = np.array([325, 120])
            P02 = np.array([375, 190])
            P03 = np.array([575, 300])

            control_points_1 = np.array([P00, P01, P02, P03])

            path_1 = bezier_curve.draw_line(control_points_1, 10)

            # Second path
            P10 = np.array([575, 300])
            P11 = np.array([800, 430])
            P12 = np.array([550, 700])
            P13 = np.array([390, 450])

            control_points_2 = np.array([P10, P11, P12, P13])

            path_2 = bezier_curve.draw_line(control_points_2, 25)

            final_path = np.vstack((path_1, path_2))

            return final_path
        
        def formation_entry(enemy):
            cx, cy = enemy.path[-1][0], enemy.path[-1][1]
            fx, fy = enemy.formation[0], enemy.formation[1]
            # First Path
            P00 = np.array([cx, cy])
            P01 = np.array([350, 390])
            P02 = np.array([350, 370])
            P03 = np.array([fx, fy+50])

            control_points_1 = np.array([P00, P01, P02, P03])

            path_1 = bezier_curve.draw_line(control_points_1, 15)[:-5]

            # Second path
            cx, cy = path_1[-1][0], path_1[-1][1]
            P10 = np.array([cx, cy])
            P11 = np.array([fx, fy+50])
            P12 = np.array([fx, fy+25])
            P13 = np.array([fx, fy])

            control_points_2 = np.array([P10, P11, P12, P13])

            path_2 = bezier_curve.draw_line(control_points_2, 10)

            final_path = np.vstack((path_1, path_2))

            return final_path
