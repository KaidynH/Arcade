import pygame

class Bullet:
    def __init__(self, player):
        # center coordinates of the bullet originate at the front of the ship
        self.cx, self.cy = player.angle_pos_dic.get(player.angle)[0][0], player.angle_pos_dic.get(player.angle)[0][1]

        # slope of the bullet is the same as the slope of the ship
        self.run, self.rise = player.calculate_slope()

        # Variable used to give the bullet a certain range
        self.range = 0.001

        # Size of the bullet
        self.size = 1
    
    # Wrap movement
    def check_wall(self):
        if self.cx >= 1200:
            self.cx = 1
        if self.cx <= 0:
            self.cx = 1199
        if self.cy >= 800:
            self.cy = 1
        if self.cy <= 0:
            self.cy = 799

    def move(self):
        # moves the center coordinates of the bullet
        self.cx += self.run * 2
        self.cy += self.rise * 2
        # Wrap movement
        self.check_wall()
        # Give bullet a certain range
        self.range += 0.004

    

    def draw(self, screen):
        # draws the bullet to the screen
        pygame.draw.circle(screen, (255,255,255), (self.cx, self.cy), self.size)
    
    
    # Runs bullet actions
    def action(self, screen, bullet, bullet_list):
        bullet.draw(screen) 
        bullet.move()
        # Delete the bullet if it has reached its max range
        if bullet.range >= 0.7:
            bullet_list.remove(bullet)


    