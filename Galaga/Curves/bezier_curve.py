import numpy as np

def cubic_bezier(t, P0, P1, P2, P3):
    return (1-t)**3 * P0 + 3 * (1-t)**2 * t * P1 + 3 * (1-t) * t**2 * P2 + t**3 * P3


def draw_line(control_points, t):
    t_values = np.linspace(0, 1, t)
    curve_points = np.array([cubic_bezier(t, *control_points) for t in t_values])
    curve_points = np.round(curve_points)
    return curve_points