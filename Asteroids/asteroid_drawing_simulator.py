import pygame, random, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption('Asteroids')

def distance(p1x, p1y, p2x, p2y):
    return ((p2x-p1x)**2 + (p2y-p1y)**2)**0.5

def check_quadrant(x, y, cx, cy):
    if x - cx > 0 and y -cy < 0:
        return 1
    elif x - cx < 0 and y -cy < 0:
        return 2
    elif x - cx > 0 and y -cy < 0:
        return 3
    elif x - cx > 0 and y -cy < 0:
        return 4
    else:
        if x - cx > 0:
            return '+x'
        elif x - cx < 0:
            return '-x'
        elif y - cx < 0:
            return '+y'
        else:
            return '-x'
    

    

white = (255,255,255)
black = (0,0,0)
outer = 30
inner = random.randint(22,24)

line_bx = 570
line_by = 400

line_sx = 570
line_sy = 400

line_ex = 570
line_ey = 400

# List of vertice points on the asteroid
points = [(570, 400)]

# asteroid center coordinates
cx = 600
cy = 400
center = (cx, cy)

# Outline of the asteroid
pygame.draw.circle(screen, white, (cx,cy), outer, width = 1)
pygame.draw.circle(screen, white, (cx,cy), inner, width = 1)

# Make the points
# for i in range(20):

# Outer to inner border line
while distance(line_ex, line_ey, cx, cy) > inner:
    quad = check_quadrant(line_ex, line_ey, cx, cy)
    if quad == 1 or quad == 4 or quad == '+x':
        x_change = random.uniform(0.05, 0.1)
        line_ex -= x_change
        line_ey += x_change
    elif quad == 2  or quad == 3 or quad == '-x':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey -= x_change
    elif quad == '+y':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey += x_change
    elif quad == '-y':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey += x_change
points.append((line_ex, line_ey))
    
# Inner to outer border line
while distance(line_ex, line_ey, cx, cy) < outer:
    quad = check_quadrant(line_ex, line_ey, cx, cy)
    if quad == 1 or quad == 4 or quad == '+x':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey += x_change / 3
    elif quad == 2  or quad == 3 or quad == '-x':
        x_change = random.uniform(0.05, 0.1)
        line_ex -= x_change
        line_ey -= x_change / 3
    elif quad == '+y':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey -= x_change / 3
    elif quad == '-y':
        x_change = random.uniform(0.05, 0.1)
        line_ex -= x_change
        line_ey += x_change / 3
points.append((line_ex, line_ey))
    
while distance(line_ex, line_ey, cx, cy) > inner:
    quad = check_quadrant(line_ex, line_ey, cx, cy)
    if quad == 1 or quad == 4 or quad == '+x':
        x_change = random.uniform(0.05, 0.1)
        line_ex -= x_change
        line_ey += x_change
    elif quad == 2  or quad == 3 or quad == '-x':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey -= x_change / 3
    elif quad == '+y':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey += x_change
    elif quad == '-y':
        x_change = random.uniform(0.05, 0.1)
        line_ex += x_change
        line_ey += x_change
points.append((line_ex, line_ey))


# points.append((line_ex, line_ey))

# Draw the lines
for i in range(len(points)-1):
    pygame.draw.line(screen, white, points[i], points[i+1])

# pygame.draw.line(screen, white, points[-1], points[0])



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

