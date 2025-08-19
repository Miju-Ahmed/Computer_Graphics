import numpy as np
import matplotlib.pyplot as plt

def branch(p1, length, angle, depth, ax):
    if depth == 0:
        return
    
    # Compute endpoint of this branch
    dx = length * np.cos(angle)
    dy = length * np.sin(angle)
    p2 = (p1[0] + dx, p1[1] + dy)
    
    # Draw the branch
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green', linewidth=depth)
    
    # Branch angles
    angle_left = angle + np.pi/6   # 30 degrees left
    angle_right = angle - np.pi/6  # 30 degrees right
    
    # Shorter branches
    new_length = length * 0.7
    
    # Recurse for left and right branches
    branch(p2, new_length, angle_left, depth - 1, ax)
    branch(p2, new_length, angle_right, depth - 1, ax)

if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(8,8))
    
    # Start point and parameters
    start_point = (0, 0)
    initial_length = 1.0
    initial_angle = np.pi/2  # Straight up
    
    # Generate fractal tree
    branch(start_point, initial_length, initial_angle, depth=10, ax=ax)
    
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()
    fig.savefig("fractal_tree.png", dpi=300, bbox_inches='tight')
