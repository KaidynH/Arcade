import pygame, random

class Asteroid:
    def __init__(self, wall, size, asteroid='none'):
        # radius of the asteroid
        self.size = size
        # Limits the number of splits per asteroid
        self.splits = 0
        # Initialize an asteroid along one of the walls
        if wall == 'left':
            # Center coordinates
            self.cx = 20
            self.cy = random.randint(20,780)
            # Movement variables
            self.run = random.uniform(.2,.3)
            # Down movement
            if self.coin_toss() == 1:
                self.rise = random.uniform(.2,.3)
            # Up movement
            else:
                self.rise = random.uniform(-.3,-.2)
        elif wall == 'right':
            self.cx = 1180
            self.cy = random.randint(20,780)
            # Movement variables
            self.run = random.uniform(-.3,-.2)
            # Down movement
            if self.coin_toss == 1:
                self.rise = random.uniform(.2,.3)
            # Up movement
            else:
                self.rise = random.uniform(-.3,-.2)
        elif wall == 'top':
            self.cx = random.randint(20,1180)
            self.cy = 20
            # Movement variables
            self.rise = random.uniform(.2,.3)
            # Right movement
            if self.coin_toss() == 1:
                self.run = random.uniform(.2,.3)
            # Left movement
            else:
                self.run = random.uniform(-.3,-.2)
        elif wall == 'bottom':
            self.cx = random.randint(20,1180)
            self.cy = 780
            # Movement variables
            self.rise = random.uniform(-.2,-.3)
            # Right movement
            if self.coin_toss() == 1:
                self.run = random.uniform(.2,.3)
            # Left movement
            else:
                self.run = random.uniform(-.3,-.2)
        # This else statement is used during splits
        else:
            self.cx = asteroid.cx
            self.cy = asteroid.cy
            self.splits = asteroid.splits + 1
            # New asteroids have random movement direction and a speed greater than parent asteroid
            # This variables is used to increase the speed a certain amount based on the size of the asteroid
            speed_multiplier = 1
            if asteroid.size == 30:
                speed_multiplier = 1.5
            if asteroid.size == 15:
                speed_multiplier = 2
            # Right movement
            if self.coin_toss() == 1:
                self.run = random.uniform(0.2,0.3) * speed_multiplier
            # Left movement
            else:
                self.run = random.uniform(-0.3,-0.2) * speed_multiplier
            # Down movement
            if self.coin_toss() == 1:
                self.rise = random.uniform(0.2,0.3) * speed_multiplier
            # Up movement
            else:
                self.rise = random.uniform(-0.3,-0.2) * speed_multiplier

    # Returns 1 or 2 representing heads or tails
    def coin_toss(self):
        return random.randint(1,2)

    # Wrap movement if the asteroid hits a wall
    def check_wall(self):
        # Right wall
        if self.cx >= 1200:
            self.cx = 1
        # Left wall
        if self.cx <= 0:
            self.cx = 1199
        # Bottom wall
        if self.cy >= 800:
            self.cy = 1
        # Top wall
        if self.cy <= 0:
            self.cy = 799

    # Draw the asteroid to the screen
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.cx, self.cy), self.size)
    
    # Move the asteroid
    def move(self):
        # Horizontal movement
        self.cx += self.run
        # Vertical movement
        self.cy += self.rise
        # Wrap movement
        self.check_wall()

    # Splits the asteroid in two
    def split(self, asteroid_list, asteroid):
        # Asteroids' movement are randomized in the final else statement of the initialize class
        # First asteroid set to half the size of the original
        asteroid_list.append(Asteroid('none', asteroid.size/2, asteroid))
        # Second asteroid set to half the size of the original
        asteroid_list.append(Asteroid('none', asteroid.size/2, asteroid))
        # Delete the original asteroid
        # If statement used to fix an issue
        if asteroid in asteroid_list:
            asteroid_list.remove(asteroid)

    def check_collision(self, bullet_list, asteroid_list, asteroid, player):
        for bullet in bullet_list[:]:
            # Check if the distance between the bullet and the asteroid is less than the sum of the two sizes
            # If they are, a bullet has collided with an asteroid
            if ((self.cx - bullet.cx)**2 + (self.cy - bullet.cy)**2)**(1/2) <= self.size + bullet.size:
                # Add a certain score the player score depending on the asteroid's size
                # Big asteroids are worth 20 points
                if self.size == 30:
                    player.score += 20
                # Medium asteroids are worth 50 points
                elif self.size == 15:
                    player.score += 50
                # Small asteroids are worth 100 points
                else:
                    player.score += 100
                # Delete the bullet when it hits
                bullet_list.remove(bullet)
                # Delete the asteroid without splitting if it is a small asteroid
                if self.splits == 2 and asteroid in asteroid_list:
                    asteroid_list.remove(asteroid)
                # Split the asteroid if it is a big or small asteroid
                else:
                    self.split(asteroid_list, asteroid)
                break
                
    

    # Runs asteroid actions
    def action(self, screen, asteroid, asteroid_list, bullet_list, player):
        asteroid.draw(screen)
        asteroid.move()
        asteroid.check_collision(bullet_list, asteroid_list, asteroid, player)
    


