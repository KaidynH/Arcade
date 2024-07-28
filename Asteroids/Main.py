import pygame, random
from tinydb import TinyDB, Query
from player_class import Player
from bullet_class import Bullet
from asteroid_class import Asteroid
from text_class import Text

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Asteroids')

def display_text(text_list):
    for text in text_list:
        text.blit_text(screen)

# List of keys, returns true for each key pressed, and false for the ones that aren't
keys = pygame.key.get_pressed()

# Initialize a highscore database
highscores_database = TinyDB('db.json')

# Query used in database
Score = Query()

# Used to run the home screen
home_runner = True

# List of wall choices
wall_list = ['left', 'right', 'top', 'bottom']

# List of asteroids
asteroid_list = [Asteroid(random.choice(wall_list), 30, 'none'), Asteroid(random.choice(wall_list), 30, 'none'), Asteroid(random.choice(wall_list), 30, 'none'), Asteroid(random.choice(wall_list), 30, 'none')]

# List of bullets
bullet_list = []

# Ship variable
player = Player(600, 400, 90)

# Code and comments used to set up and display text and font variables are from the following website:
# GfG
# GfG. (2022). Python: Display text to PyGame window. 
# Retrieved from https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

# Text dislay variables

# Press space to play
press_space_text = Text('freesansbold.ttf', 30, 'PRESS SPACE TO PLAY', (255,255,255), 600, 650)

# Press i for instructions
press_i_text = Text('freesansbold.ttf', 15, 'PRESS I FOR INSTRUCTIONS', (255,255,255), 600, 700)

# Instructions text variables

# Forward movement
foraward_movement_text = Text('freesansbold.ttf', 15, 'PRESS THE UP ARROW TO MOVE THE SHIP FORWARD', (255,255,255), 650, 300)

# CW rotation
CW_rotation_text = Text('freesansbold.ttf', 15, 'PRESS THE RIGHT ARROW TO ROTATE CLOCKWISE', (255,255,255), 650, 350)

# CCW rotation
CCW_rotation_text = Text('freesansbold.ttf', 15, 'PRESS THE LEFT ARROW TO ROTATE COUNTER-CLOCKWISE', (255,255,255), 650, 400)

# Hyperspace
hyperspace_text = Text('freesansbold.ttf', 15, 'PRESS THE DOWN ARROW TO SEND THE SHIP INTO HYPERSPACE', (255,255,255), 650, 450)

# Shooting
shooting_text = Text('freesansbold.ttf', 15, 'PRESS THE SPACE BAR TO SHOOT', (255,255,255), 650, 500)

# Instructions graphics
up_arrow = Player(425, 300, 90)
right_arrow = Player(430, 350, 0)
left_arrow = Player(395, 400, 180)
down_arrow = Player(385, 450, 270)

# Movement test
movement_test_text = Text('freesansbold.ttf', 15, 'PRESS T TO TRY OUT THE MOVEMENT BEFORE YOU PLAY', (255,255,255), 650, 700)

# Instructions and Movement Test exit
exit_text = Text('freesansbold.ttf', 15, 'PRESS Q TO RETURN TO THE HOME SCREEN', (255,255,255), 650, 750)

# Hishscore rank text display

# Rank 1
rank_1_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=2).get('rank')), (255,255,255), 500, 100), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=2).get('score')), (255,255,255), 600, 100), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=2).get('initials')), (255,255,255), 700, 100)]

# Rank 2
rank_2_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=3).get('rank')), (255,255,255), 500, 150), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=3).get('score')), (255,255,255), 600, 150), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=3).get('initials')), (255,255,255), 700, 150)]

# Rank 3
rank_3_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=4).get('rank')), (255,255,255), 500, 200), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=4).get('score')), (255,255,255), 600, 200), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=4).get('initials')), (255,255,255), 700, 200)]

# Rank 4
rank_4_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=5).get('rank')), (255,255,255), 500, 250), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=5).get('score')), (255,255,255), 600, 250), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=5).get('initials')), (255,255,255), 700, 250)]

# Rank 5
rank_5_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=6).get('rank')), (255,255,255), 500, 300), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=6).get('score')), (255,255,255), 600, 300), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=6).get('initials')), (255,255,255), 700, 300)]

# Rank 6
rank_6_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=7).get('rank')), (255,255,255), 500, 350), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=7).get('score')), (255,255,255), 600, 350), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=7).get('initials')), (255,255,255), 700, 350)]

# Rank 7
rank_7_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=8).get('rank')), (255,255,255), 500, 400), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=8).get('score')), (255,255,255), 600, 400), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=8).get('initials')), (255,255,255), 700, 400)]

# Rank 8
rank_8_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=9).get('rank')), (255,255,255), 500, 450), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=9).get('score')), (255,255,255), 600, 450), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=9).get('initials')), (255,255,255), 700, 450)]

# Rank 9
rank_9_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=10).get('rank')), (255,255,255), 500, 500), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=10).get('score')), (255,255,255), 600, 500), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=10).get('initials')), (255,255,255), 700, 500)]

# Rank 10
rank_10_text = [Text('freesansbold.ttf', 20, str(highscores_database.get(doc_id=11).get('rank')), (255,255,255), 500, 550), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=11).get('score')), (255,255,255), 600, 550), Text('freesansbold.ttf', 15, str(highscores_database.get(doc_id=11).get('initials')), (255,255,255), 700, 550)]

rank_text_list = [rank_1_text, rank_2_text, rank_3_text, rank_4_text, rank_5_text, rank_6_text, rank_7_text, rank_8_text, rank_9_text, rank_10_text, ]
# Runs the home screen
while home_runner:
    # Clear the screen before drawing
    screen.fill((0,0,0))

    # Display the words, "Press Space to play"
    # copying the text surface object to the screen at the center coordinate of the text rectangle
    press_space_text.blit_text(screen)

    # Display the words, "Press I for instructions"
    press_i_text.blit_text(screen)

    # Display the ranks to the screen
    for i in range(2,12):
        if highscores_database.get(doc_id=i).get('score') != 0:
            display_text(rank_text_list[i-2])



    # Draw and move asteroids in the background
    for asteroid in asteroid_list:
        asteroid.draw(screen)
        asteroid.move()
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Starts running the game when the space bar is pressed
            if event.key == pygame.K_SPACE:
                player.game_runner = True
                home_runner = False
            # Starts running the instructions screen when I is pressed
            if event.key == pygame.K_i:
                instructions_runner = True
                while instructions_runner:
                    screen.fill((0,0,0))
                    
                    # Display the instructions text
                    foraward_movement_text.blit_text(screen)
                    CW_rotation_text.blit_text(screen)
                    CCW_rotation_text.blit_text(screen)
                    hyperspace_text.blit_text(screen)
                    shooting_text.blit_text(screen)
                    movement_test_text.blit_text(screen)
                    exit_text.blit_text(screen)

                    # Display the instructions graphics
                    up_arrow.draw(screen)
                    right_arrow.draw(screen)
                    left_arrow.draw(screen)
                    down_arrow.draw(screen)
                    # Rectangle represents space bar
                    pygame.draw.rect(screen, (255,255,255), (450, 495, 50, 10), width=1)

            
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            # Stops running the instruction screen when Q is pressed
                            if event.key == pygame.K_q:
                                instructions_runner = False
                            # Starts running the movement test runner when t is pressed on the instructions page
                            if event.key == pygame.K_t:
                                movement_test_runner = True
                                while movement_test_runner:
                                    screen.fill((0,0,0))
                                    
                                    # Runs the player actions
                                    player.action(screen, player)

                                    # Display the exit text
                                    exit_text.blit_text(screen)

                                    for event in pygame.event.get():
                                        if event.type == pygame.KEYDOWN:
                                            # Create a bullet when space bar is pressed
                                            if event.key == pygame.K_SPACE:
                                                bullet_list.append(Bullet(player))
                                            # Stops running the movement test runner when q is pressed
                                            if event.key == pygame.K_q:
                                                movement_test_runner = False
                                    
                                    # Run bullet actions
                                    for bullet in bullet_list[:]:
                                        bullet.action(screen, bullet, bullet_list)

                                    pygame.display.update()
                                    pygame.time.delay(5)


                    pygame.display.update()
                    pygame.time.delay(5)
    
    pygame.display.update()
    pygame.time.delay(5)

# Reset the ship incase it was moved in instructions
player.cx = 600
player.cy = 400
player.angle = 90

# Variable used to add extra lives throughot the game
extra_life_check = 0

# Lists need reset from instructions screen

# List of bullets
bullet_list = []

# List of asteroids
asteroid_list = []

# List of player objects to display the number of lives
life_display_list = [Player(50, 35, 90), Player(65, 35, 90), Player(80, 35, 90)]

# Round Number
round_num = 0


# Score display variables. Explanation for text variables written in previous comments
score_text = Text('freesansbold.ttf', 15, '0', (255,255,255), 50, 10)

# Runs the game
while player.game_runner:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Create a bullet when space bar is pressed
            if event.key == pygame.K_SPACE:
                bullet_list.append(Bullet(player))
            # Send the ship into hyperspace when the down arrow is pressed
            if event.key == pygame.K_DOWN:
                player.hyperspace()
    # Clear the screen before drawing
    screen.fill((0,0,0))

    # Display the number of lives
    for life in life_display_list:
        life.draw(screen)

    # Update the score display text
    score_text = Text('freesansbold.ttf', 15, str(player.score), (255,255,255), 50, 10)

    # Concatenate the score to the screen
    score_text.blit_text(screen)

    # Adds to the round number when all the asteroids are destroyed
    if len(asteroid_list) == 0:
        round_num += 1
        # Determines a certain amount of asteroids based on the round number
        if round_num == 1:
            asteroid_num = 4
        elif round_num == 2:
            asteroid_num = 6
        elif round_num == 3:
            asteroid_num = 8
        elif round_num == 4 or round_num == 5:
            asteroid_num = 10
        elif round_num >= 6 or round_num <= 10:
            asteroid_num = 11
        else:
            asteroid_num = 12
        # Adds the desired number of asteroids to the asteroid list
        for i in range(asteroid_num):
            asteroid_list.append(Asteroid(random.choice(wall_list), 30))
        
    # Check if the ship has hit any asteroids
    player.check_collision(asteroid_list)

    # Run player actions if the ship is alive
    if player.alive:
        player.action(screen, player)
    # Runs the death animation if the player is dead
    else:
        if len(life_display_list) > 0:
            life_display_list.remove(life_display_list[-1])
        player.death_animation(screen, (player.fx,player.fy), (player.brx,player.bry), (player.blx,player.bly), (player.b_mpx, player.b_mpy), asteroid_list, bullet_list, score_text, life_display_list)
 

    # Run asteroid actions
    for asteroid in asteroid_list[:]:
        asteroid.action(screen, asteroid, asteroid_list, bullet_list, player)

    # Run bullet actions
    for bullet in bullet_list[:]:
        bullet.action(screen, bullet, bullet_list)
    
    # Add an extra life to the ship for every ten thousand points
    # Tests if the floor of the score divided by ten thousand is greater than the extra life check variable
    if player.score // 10000 > extra_life_check:
        # Add an extra life
        player.lives += 1
        # Add one to the extra life check
        extra_life_check += 1
        # Update the life display list
        if len(life_display_list) == 0:
            life_display_list.append(Player(50, 35, 90))
        else:
            life_display_list.append(Player(life_display_list[-1].cx + 15, 35, 90))
    
    pygame.display.update()
    pygame.time.delay(5)


# Game over screen text variables

# High score message
highscore_message = Text('freesansbold.ttf', 20, 'YOUR SCORE IS ONE OF THE TEN BEST', (255,255,255), 600, 500)

# Instructions message 1
high_core_instruction_text1 = Text('freesansbold.ttf', 20, 'PLEASE ENTER YOUR INITIALS', (255,255,255), 600, 550)

# Instructions message 2
highscore_instruction_text2 = Text('freesansbold.ttf', 20, 'PRESS THE UP ARROW TO MOVE FORWARD THROUGH THE ALPHABET', (255,255,255), 600, 600)

# Instructions message 3
highscore_instruction_text3 = Text('freesansbold.ttf', 20, 'PRESS THE DOWN ARROW TO MOVE BACKWARDS THROUGH THE ALPHABET', (255,255,255), 600, 650)

# Instruction mesage 4
highscore_instruction_text4 = Text('freesansbold.ttf', 20, 'PRESS SPACE TO SELECT THE LETTER', (255,255,255), 600, 700)

highscore_text_list = [highscore_message, high_core_instruction_text1, highscore_instruction_text2, highscore_instruction_text3, highscore_instruction_text4]

# Initials
initials_text_list = [Text('freesansbold.ttf', 40, '_', (255,255,255), 550, 400), Text('freesansbold.ttf', 40, '_', (255,255,255), 600, 400), Text('freesansbold.ttf', 40, '_', (255,255,255), 650, 400)]



# Runs the game over screen
while player.game_over_runner:
    # Clear the scren before drawing
    screen.fill((0,0,0))

    # Concatenate the instructions messages to the screen
    display_text(highscore_text_list)

    # Concatenate the initials to the screen
    display_text(initials_text_list)

    # Initial selection variables
    # List of uppercase letters in the alphabet cycled through during selection
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # The current initial being selected
    current_letter = ''
    # The initals
    initials = ''
    # The index used when cycling through through the alphabet list
    alpha_index = -1

    initials_list = ['_', '_', '_']

    # Initial selection if player score is higher than the lowest high score 
    if player.score > highscores_database.get(doc_id=11).get('score'):
        # Select initials until all three are selected
        while len(initials) < 3:
            for event in pygame.event.get():
                screen.fill((0,0,0))
                # Concatenate the instructions messages to the screen
                display_text(highscore_text_list)
                # Concatenate the initials to the screen
                display_text(initials_text_list)


                if event.type == pygame.KEYDOWN:

                    # Move forwards the through the alphabet list
                    if event.key == pygame.K_UP:
                        if alpha_index == 25:
                            alpha_index = 0
                        else:
                            alpha_index += 1
                        current_letter = alphabet[alpha_index]
                        initials_list[len(initials)] = current_letter
                        for i in range(3):
                            initials_text_list[i].text = initials_list[i]


                    # Move backwards through the alphabet list
                    if event.key == pygame.K_DOWN:
                        if alpha_index == -26:
                            alpha_index = 25
                        else:
                            alpha_index -= 1
                        current_letter = alphabet[alpha_index]
                        initials_list[len(initials)] = current_letter
                        for i in range(3):
                            initials_text_list[i].text = initials_list[i]
                    # Add the current letter to the initials
                    if event.key == pygame.K_SPACE:
                        initials += current_letter
                        current_letter = 'A'
                        alpha_index = 0
                        try:
                            initials_text_list[len(initials)].text = 'A'
                        except:
                            pass
                        display_text(initials_text_list)
            pygame.display.update()
            pygame.time.delay(5)
            
    # Loops through every score in the highscore database
    for score in highscores_database.all():
        # checks if the player score is greater than the score
        if player.score > score.get('score'):
            # A list of ranks below the rank being changed
            need_changed = []

            # Change the rank being changed to negative 1
            highscores_database.update({'rank':-1}, doc_ids=[score.get('rank')+1])

            # Add all the ranks that need changed to the list
            for s in highscores_database.all():
                if s.get('rank') > score.get('rank'):
                    need_changed.append(s.doc_id)

            # Reverse the list so it cycles through starting with the lowest rank
            need_changed.reverse()

            # Move all the scores that need changed down one
            for id in need_changed:
                highscores_database.update({'score':highscores_database.get(doc_id=id-1).get('score'), 'initials':highscores_database.get(doc_id=id-1).get('initials')}, doc_ids=[id])

            # Update the rank that needs changed
            highscores_database.update({'score':player.score, 'initials':initials}, Score.rank == -1)
            highscores_database.update({'rank':score.get('rank')}, Score.rank == -1)
            break
    
    # Turn off the game over screen
    player.game_over_runner = False

    pygame.display.update()
    pygame.time.delay(5)


pygame.display.update()
pygame.time.delay(5)


