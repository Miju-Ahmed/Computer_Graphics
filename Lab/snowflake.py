import matplotlib.pyplot as plt
import numpy as np

def koch_snowflake(order, scale=10):
    """
    Returns the coordinates of the Koch snowflake of given order.
    """
    # Initial equilateral triangle
    def initial_triangle(scale):
        # Equilateral triangle vertices (upward triangle)
        p1 = np.array([0, 0])
        p2 = np.array([scale, 0])
        p3 = np.array([scale/2, scale*np.sqrt(3)/2])
        return np.array([p1, p2, p3, p1])

    def koch_iteration(points):
        new_points = []
        for i in range(len(points)-1):
            p1 = points[i]
            p2 = points[i+1]
            delta = (p2 - p1) / 3.0
            pa = p1 + delta
            pb = p1 + 2*delta

            # rotate delta by -60° (clockwise)
            angle = -np.pi / 3
            peak = pa + np.array([
                delta[0]*np.cos(angle) - delta[1]*np.sin(angle),
                delta[0]*np.sin(angle) + delta[1]*np.cos(angle)
            ])

            new_points.extend([p1, pa, peak, pb])
        new_points.append(points[-1])
        return np.array(new_points)

    points = initial_triangle(scale)
    for _ in range(order):
        points = koch_iteration(points)
    return points


# Plot Koch snowflake iterations
orders = [0, 1, 2, 3, 4, 5]
fig, axes = plt.subplots(1, len(orders), figsize=(15, 3))

for ax, order in zip(axes, orders):
    points = koch_snowflake(order)
    ax.plot(points[:, 0], points[:, 1], color="blue")
    ax.set_aspect('equal')
    ax.axis("off")
    ax.set_title(f"Order {order}")

plt.show()
