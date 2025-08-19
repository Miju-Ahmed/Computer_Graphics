import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def bezier_curve(control_points, n_points=100):
    n = len(control_points) - 1
    if n < 1:
        raise ValueError("A Bézier curve requires at least two control points.")
    control_points = np.array(control_points, dtype=float)
    t = np.linspace(0, 1, n_points)
    curve = np.zeros((n_points, 2)) 
    for i in range(n + 1):
        bernstein_poly = comb(n, i) * (t**i) * ((1 - t)**(n - i))
        curve += np.outer(bernstein_poly, control_points[i])
    return curve

def plot_artwork_with_controls(artwork_parts, title, color='black'):
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    for part in artwork_parts:
        curve = bezier_curve(part)
        plt.plot(curve[:, 0], curve[:, 1], color=color, lw=3, label='Bézier Curve')
        points = np.array(part)
        plt.plot(points[:, 0], points[:, 1], 'ro--', lw=1, markersize=5, label='Control Polygon')

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    
    plt.title(title, fontsize=18)
    plt.grid(True) 
    ax.set_aspect('equal', adjustable='box')
    plt.show()

def create_swan():
    swan_parts = [
        [
            (10, 50), (40, 10), (80, 20), (95, 60)
        ],
        [
            (95, 60), (110, 140), (40, 110), (60, 80)
        ]
    ]
    
    plot_artwork_with_controls(swan_parts, title="Bézier Swan with Control Points")

def create_butterfly():
    right_wing_parts = [
        [
            (5, 0), (60, 100), (100, 80), (40, -10)
        ],
        [
            (40, -10), (80, -60), (20, -80), (5, -20)
        ]
    ]

    left_wing_parts = []
    for part in right_wing_parts:
        reflected_part = [(-x, y) for x, y in part]
        left_wing_parts.append(reflected_part)
        
    all_parts = right_wing_parts + left_wing_parts
    
    plot_artwork_with_controls(all_parts, title="Bézier Butterfly with Control Points", color='#003366')

if __name__ == '__main__':
    create_swan()
    create_butterfly()