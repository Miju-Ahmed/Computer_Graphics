import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def beizer_curve(control_points,n_points=100):
    n=len(control_points)-1
    if(n<1):
        raise ValueError("At least two points are required.")
    control_points=np.array(control_points,dtype=float)
    t=np.linspace(0,1,n_points)
    curve=np.zeros((n_points,2))
    for i in range(n+1):
        bernstein_ply=comb(n,i)*(t**i)*((1-t)**(n-i))
        curve+=np.outer(bernstein_ply,control_points[i])
    return curve


if __name__ == '__main__':
    # --- Control Points for a Human Shape ---
    # Each list of tuples is a separate Bézier curve for a body part.
    
    human_parts = {
        'head': [
            (180, 400),  # P0: Start of head arc
            (200, 450),  # P1: Top of head
            (220, 400),  # P2: End of head arc
        ],
        'torso': [
            (200, 400),  # P0: Neck
            (200, 320),  # P1: Upper torso control
            (200, 250),  # P2: Lower torso control
            (200, 180),  # P3: Hips
        ],
        'left_arm': [
            (200, 370),  # P0: Shoulder
            (150, 350),  # P1: Elbow area
            (130, 280),  # P2: Forearm area
            (150, 250),  # P3: Hand
        ],
        'right_arm': [
            (200, 370),  # P0: Shoulder
            (250, 350),  # P1: Elbow area
            (270, 280),  # P2: Forearm area
            (250, 250),  # P3: Hand
        ],
        'left_leg': [
            (200, 180),  # P0: Hip
            (180, 100),  # P1: Knee area
            (180, 50),   # P2: Ankle area
            (200, 0),    # P3: Foot
        ],
        'right_leg': [
            (200, 180),  # P0: Hip
            (220, 100),  # P1: Knee area
            (220, 50),   # P2: Ankle area
            (200, 0),    # P3: Foot
        ],
    }
    
    # --- Plotting the Figure ---
    plt.figure(figsize=(6, 10))
    ax = plt.gca()

    # Plot each body part
    for part, control_points in human_parts.items():
        curve = beizer_curve(control_points)
        plt.plot(curve[:, 0], curve[:, 1], 'b-', lw=3)

    # --- Optional: Plot control points to see how they work ---
    # Uncomment the block below to visualize the control points in red
    """
    for part, control_points in human_parts.items():
        points = np.array(control_points)
        plt.plot(points[:, 0], points[:, 1], 'ro--', lw=0.5, markersize=4, label=part)
    plt.legend()
    """

    plt.title("Human Shape with Bézier Curves", fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    ax.set_aspect('equal', adjustable='box')
    plt.show()