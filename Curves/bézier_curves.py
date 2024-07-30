import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bezier Curve Visualization")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Control points
P0 = np.array([100, 500])
P1 = np.array([200, 100])
P2 = np.array([600, 100])
P3 = np.array([700, 500])
control_points = [P0, P1, P2, P3]
selected_point = None

# Function to compute cubic Bézier point
def cubic_bezier(t, P0, P1, P2, P3):
    return (1-t)**3 * P0 + 3 * (1-t)**2 * t * P1 + 3 * (1-t) * t**2 * P2 + t**3 * P3

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = np.array(pygame.mouse.get_pos())
            for i, point in enumerate(control_points):
                if np.linalg.norm(point - mouse_pos) < 10:
                    selected_point = i
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_point = None
        elif event.type == pygame.MOUSEMOTION and selected_point is not None:
            control_points[selected_point] = np.array(pygame.mouse.get_pos())

    # Clear screen
    window.fill(white)

    # Draw Bézier curve
    t_values = np.linspace(0, 1, 100)
    curve_points = np.array([cubic_bezier(t, *control_points) for t in t_values])
    pygame.draw.lines(window, black, False, curve_points, 2)

    # Draw control points and lines
    for point in control_points:
        pygame.draw.circle(window, red, point, 5)
    pygame.draw.lines(window, green, False, control_points, 1)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
