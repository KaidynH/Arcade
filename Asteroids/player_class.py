import pygame, random

class Player:
    def __init__(self, cx, cy, angle):
        # Runs the game
        self.game_runner = True

        # Runs the game over screen
        self.game_over_runner = False

        # Center coridinates
        self.cx = cx
        self.cy = cy

        # Interval varibales used to slow down rotation and speed up rate
        self.rotate_interval = 0.0001
        self.speed_interval = 0.0001

        # Slope of forward movement
        self.run = 0
        self.rise = 0

        # Used to speed up the speed
        self.multiplier = 1.1

        # Angle of the front of the ship's point of the triangle from the center point
        self.angle = angle

        # Dictionary of triangle coordinates for every angle
        self.define_apd()

        # Determine if the ship is alive
        self.alive = True

        # Limits the number of lives
        self.lives = 3

        # Player score
        self.score = 0
    

    # Redefines the dictionary of triangle coordinates for every angle
    def define_apd(self):
        self.angle_pos_dic = {
            0:[(self.cx+10,self.cy), (self.cx-10*(3**(1/2)/2),self.cy-5), (self.cx-10*(3**(1/2)/2),self.cy+5)],
            30:[(self.cx+10*(3**(1/2)/2),self.cy-5), (self.cx-10,self.cy), (self.cx-5,self.cy+10*(3**(1/2)/2))],
            60:[(self.cx+5,self.cy-10*(3**(1/2)/2)), (self.cx-10*(3**(1/2)/2),self.cy+5), (self.cx,self.cy+10)],
            90:[(self.cx,self.cy-10), (self.cx-5,self.cy+10*(3**(1/2)/2)), (self.cx+5,self.cy+10*(3**(1/2)/2))],
            120:[(self.cx-5,self.cy-10*(3**(1/2)/2)), (self.cx,self.cy+10), (self.cx+10*(3**(1/2)/2),self.cy+5)],
            150:[(self.cx-10*(3**(1/2)/2),self.cy-5), (self.cx+5, self.cy+10*(3**(1/2)/2)), (self.cx+10, self.cy)],
            180:[(self.cx-10,self.cy), (self.cx+10*(3**(1/2)/2),self.cy+5), (self.cx+10*(3**(1/2)/2),self.cy-5)],
            210:[(self.cx-10*(3**(1/2)/2),self.cy+5), (self.cx+10,self.cy), (self.cx+5,self.cy-10*(3**(1/2)/2))],
            240:[(self.cx-5,self.cy+10*(3**(1/2)/2)), (self.cx+10*(3**(1/2)/2),self.cy-5), (self.cx,self.cy-10)],
            270:[(self.cx,self.cy+10), (self.cx+5,self.cy-10*(3**(1/2)/2)), (self.cx-5,self.cy-10*(3**(1/2)/2))],
            300:[(self.cx+5,self.cy+10*(3**(1/2)/2)), (self.cx,self.cy-10), (self.cx-10*(3**(1/2)/2),self.cy-5)],
            330:[(self.cx+10*(3**(1/2)/2),self.cy+5), (self.cx-5,self.cy-10*(3**(1/2)/2)), (self.cx-10,self.cy)]
            }
        self.fx = self.angle_pos_dic.get(self.angle)[0][0]
        self.fy = self.angle_pos_dic.get(self.angle)[0][1]
        self.brx = self.angle_pos_dic.get(self.angle)[2][0]
        self.bry = self.angle_pos_dic.get(self.angle)[2][1]
        self.blx = self.angle_pos_dic.get(self.angle)[1][0]
        self.bly = self.angle_pos_dic.get(self.angle)[1][1]
        self.b_mpx = (self.angle_pos_dic.get(self.angle)[1][0]+self.angle_pos_dic.get(self.angle)[2][0])/2
        self.b_mpy = (self.angle_pos_dic.get(self.angle)[1][1]+self.angle_pos_dic.get(self.angle)[2][1])/2

    

    # Wrap ship around screen if it hits a wall
    def check_wall(self):
        if self.cx >= 1200:
            self.cx = 1
        if self.cx <= 0:
            self.cx = 1199
        if self.cy >= 800:
            self.cy = 1
        if self.cy <= 0:
            self.cy = 799
    

    # Rotates the triangle
    def rotate(self, rotation):
        # Interval used to slow down rotation speed
        self.rotate_interval = round(self.rotate_interval + 0.000001, 6)
        if float(str(self.rotate_interval)[-2:])%5 == 0:
            # Make sure the rotate variable doesn't get too high
            if self.rotate_interval > 10:
                self.rotate_interval = 0.0001
            if rotation == 'cw':
                if self.angle == 0:
                    self.angle = 330
                else:
                    self.angle -= 30
            else:
                if self.angle == 330:
                    self.angle = 0
                else:
                    self.angle += 30
        self.define_apd()
            
    

    # Spped up the ship when the up key is held down
    def speed(self):
        # Interval used to slow down the acceleration rate
        self.speed_interval = round(self.speed_interval + 0.000001, 6)
        if float(str(self.speed_interval)[-2:])%45 == 0 and self.multiplier < 2:
            self.multiplier += 0.05
        # Make sure the speed interval variable doesn't get too high
        if self.speed_interval > 10:
            self.speed_interval = 0.0001
        self.run *= self.multiplier
        self.rise *= self.multiplier
        self.cx += self.run
        self.cy += self.rise
        # Wrap ship around the screen if it hits a wall
        self.check_wall()
        # Redefine dictionary of angles and positions
        self.define_apd()
    

    # Slows down the ship until it stops after up key is released
    def slow(self):
        self.run *= 0.99
        self.rise *= 0.99
        self.cx += self.run
        self.cy += self.rise
        # Wrap ship around the screen if it hits a wall
        self.check_wall()
        # Redefine the angle-position dicitonary with the new center x and y coordinates
        self.define_apd()
        #Reset the speed multiplier
        self.multiplier = 1.1
    

    # Calculates the line the ship will follow on
    def calculate_slope(self):

        # Rise and run variables used to calculate the slope of the line the ship will move along
        run = (self.fx - self.b_mpx)/10
        rise = (self.fy - self.b_mpy)/10

        return run, rise
        
    
    # Draws the ship to the screen
    def draw(self, screen, player='none'):
        keys = pygame.key.get_pressed()
        pygame.draw.polygon(screen, (255,255,255), self.angle_pos_dic.get(self.angle), width = 1)
        # Trapezoid on bottom of triangle that makes the ship look more like a ship
        # Creation of the points used for the bottom of the trapezoid
        run = self.brx - self.blx
        rise = self.bry - self.bly
        bottom_left_x = self.blx + run * 1/5
        bottom_left_y = self.bly + rise * 1/5
        bottom_right_x = self.blx + run * 4/5
        bottom_right_y = self.bly + rise * 4/5
        # Creation of the top left point of the trapezoid
        test_run = self.brx - self.fx
        test_rise = self.bry - self.fy
        test_point_x = self.fx + test_run * 1/4
        test_point_y = self.fy + test_rise * 1/4
        run = test_point_x - bottom_left_x
        rise = test_point_y - bottom_left_y
        top_left_x = bottom_left_x + run * 1/4
        top_left_y = bottom_left_y + rise * 1/4
        # Creation of the top right point of the trapezoid
        test_run = self.blx - self.fx
        test_rise = self.bly - self.fy
        test_point_x = self.fx + test_run * 1/4
        test_point_y = self.fy + test_rise * 1/4
        run = test_point_x - bottom_right_x
        rise = test_point_y - bottom_right_y
        top_right_x = bottom_right_x + run * 1/4
        top_right_y = bottom_right_y + rise * 1/4
        # Draw the trapezoid
        pygame.draw.polygon(screen, (255,255,255), [(bottom_left_x, bottom_left_y), (bottom_right_x, bottom_right_y), (top_right_x, top_right_y), (top_left_x, top_left_y)], width = 1)
        # Black out the bottom
        pygame.draw.line(screen, (0,0,0), (bottom_left_x, bottom_left_y), (bottom_right_x, bottom_right_y))
        # Rocket blast display
        if keys[pygame.K_UP] and player == self:
            mpx = (top_left_x + top_right_x) / 2
            mpy = (top_left_y + top_right_y) / 2
            run = -self.run
            rise = -self.rise
            p3x = mpx + run * 3
            p3y = mpy + rise * 3
            pygame.draw.polygon(screen, (255,255,255), [(top_left_x,top_left_y), (top_right_x,top_right_y), (p3x,p3y)], width=1)


    # Kills ship if it hits an asteroid
    def check_collision(self, asteroid_list):
        for asteroid in asteroid_list:
            # Check if the distance between the ship and any asteroid is less than / equal to the sum of the two sizes
            if ((self.cx - asteroid.cx)**2 + (self.cy - asteroid.cy)**2)**(1/2) <= 10 + asteroid.size:
                # Kill the asteroid
                self.alive = False
                # Subtract a life
                self.lives -= 1
    
    # Animate the ship exploding when it collides with an asteroid
    def death_animation(self, screen, front_ship, br_ship, bl_ship, bmp_ship, asteroid_list, bullet_list, score_text, life_display_list):
        # Used to slow down the movement of the ship pieces
        interval = 0.001
        # 14 point variables (6 xs and 6 ys) used to draw and move three lines
        point_variables = {"Bx":front_ship[0], "Ax":br_ship[0], "Cx":bl_ship[0], "By":front_ship[1], "Ay":br_ship[1], "Cy":bl_ship[1], "bx":front_ship[0], "ax" :br_ship[0], "cx":bl_ship[0], "by":front_ship[1], "ay":br_ship[1], "cy":bl_ship[1], "Gx":bmp_ship[0], "Gy":bmp_ship[1]}
        # Line movement variables
        movement_variables = {"D_run":(point_variables.get("Ax")-point_variables.get("Bx"))/10, "D_rise":(point_variables.get("Ay") - point_variables.get("By"))/10, "E_run":(point_variables.get("Gx") - point_variables.get("Bx"))/10, "E_rise":(point_variables.get("Gy") - point_variables.get("By"))/10, "F_run":(point_variables.get("Cx") - point_variables.get("Bx"))/10, "F_rise":(point_variables.get("Cy") - point_variables.get("By"))/10}
        # Ship line variables
        ship_line_variables = { "Ds":(point_variables.get("bx"),point_variables.get("by")), "De":(point_variables.get("Ax"),point_variables.get("Ay")), "Es":(point_variables.get("ax"),point_variables.get("ay")), "Ee":(point_variables.get("Cx"),point_variables.get("Cy")), "Fs":(point_variables.get("cx"),point_variables.get("cy")), "Fe":(point_variables.get("Bx"),point_variables.get("By")),}
        # Death animation loop
        for i in range(400):
            # Slow down movement of ship parts
            interval = round(interval + .000001, 6)
            if float(str(interval)[-2:])%5 == 0:
                # Ship line variables redefined
                ship_line_variables.update({"Ds":(point_variables.get('bx'), point_variables.get("by"))})
                ship_line_variables.update({"De":(point_variables.get('Ax'), point_variables.get("Ay"))})
                ship_line_variables.update({"Es":(point_variables.get('ax'), point_variables.get("ay"))})
                ship_line_variables.update({"Ee":(point_variables.get('Cx'), point_variables.get("Cy"))})
                ship_line_variables.update({"Fs":(point_variables.get('cx'), point_variables.get("cy"))})
                ship_line_variables.update({"Fe":(point_variables.get('Bx'), point_variables.get("By"))})
                # Ship line variables moved
                point_variables.update({"bx":point_variables.get("bx") + movement_variables.get("D_run")})
                point_variables.update({"Ax":point_variables.get("Ax") + movement_variables.get("D_run")})
                point_variables.update({"by":point_variables.get("by") + movement_variables.get("D_rise")})
                point_variables.update({"Ay":point_variables.get("Ay") + movement_variables.get("D_rise")})
                point_variables.update({"ax":point_variables.get("ax") + movement_variables.get("E_run")})
                point_variables.update({"Cx":point_variables.get("Cx") + movement_variables.get("E_run")})
                point_variables.update({"ay":point_variables.get("ay") + movement_variables.get("E_rise")})
                point_variables.update({"Cy":point_variables.get("Cy") + movement_variables.get("E_rise")})
                point_variables.update({"cx":point_variables.get("cx") + movement_variables.get("F_run")})
                point_variables.update({"Bx":point_variables.get("Bx") + movement_variables.get("F_run")})
                point_variables.update({"cy":point_variables.get("cy") + movement_variables.get("F_rise")})
                point_variables.update({"By":point_variables.get("By") + movement_variables.get("F_rise")})
            # clear the screen
            screen.fill((0,0,0))
            # Draw the ship lines
            pygame.draw.line(screen, (255,255,255), ship_line_variables.get("Ds"), ship_line_variables.get("De"))
            pygame.draw.line(screen, (255,255,255), ship_line_variables.get("Es"), ship_line_variables.get("Ee"))
            pygame.draw.line(screen, (255,255,255), ship_line_variables.get("Fs"), ship_line_variables.get("Fe"))
            # Continue asteroid actions
            for asteroid in asteroid_list[:]:
                asteroid.action(screen, asteroid, asteroid_list, bullet_list, self)
            # Continue bullet actions
            for bullet in bullet_list[:]:
                bullet.action(screen, bullet, bullet_list)
            # Continue to display the number of lives
            for life in life_display_list:
                life.draw(screen, 'none')
            # Update the score display text
            score_text.text = str(self.score)

            # Display the score
            score_text.blit_text(screen)

            # Update and delay the screen
            pygame.display.update()
            pygame.time.delay(5)
        # End the game if the player is out of lives
        if self.lives == -1:
            self.game_runner = False
            self.game_over_runner = True
        # Respawn the player in the middle of the screen when the death animation is over if the player is not out of lives
        self.cx = 600
        self.cy = 400
        self.angle = 90
        self.rise = 0
        self.run = 0
        self.define_apd()
        self.alive = True


    # Moves the ship to a random location on the screen
    def hyperspace(self):
        self.cx = random.randint(20,1180)
        self.cy - random.randint(20, 780)
        self.define_apd()
        

        

    # Displays actions to the screen
    def action(self, screen, player):
        keys = pygame.key.get_pressed()

        # Clockwise Rotate
        if keys[pygame.K_RIGHT]:
            self.rotate('cw')
        
        # Counter-Clockwise Rotate
        if keys[pygame.K_LEFT]:
            self.rotate('ccw')
        
        if keys[pygame.K_UP]:
            self.run, self.rise = self.calculate_slope()
            self.speed()
        
        if not keys[pygame.K_UP] and ((self.run > .0001 or self.run < -.0001) or (self.rise > .0000001 or self.rise < -.0001)):
            self.slow()


        self.draw(screen, player)
        


        

        
    
