import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def bezier_curve(control_points, n_points=100):
    """
    Generates a Bézier curve from a set of control points.

    Args:
        control_points (list of tuples): A list of control points,
                                          where each point is a tuple (x, y).
        n_points (int): The number of points to calculate on the curve.

    Returns:
        numpy.ndarray: An array of shape (n_points, 2) representing the
                       x and y coordinates of the curve.
    """
    n = len(control_points) - 1
    if n < 1:
        raise ValueError("At least two control points are required.")

    # Convert control points to a numpy array
    control_points = np.array(control_points, dtype=float)

    # Generate the parameter t from 0 to 1
    t = np.linspace(0, 1, n_points)

    # Calculate the curve points using the general Bézier formula
    curve = np.zeros((n_points, 2))
    for i in range(n + 1):
        # Calculate the Bernstein polynomial
        bernstein_poly = comb(n, i) * (t**i) * ((1 - t)**(n - i))
        # Add the influence of the current control point
        curve += np.outer(bernstein_poly, control_points[i])

    return curve

def plot_curve_with_controls(curve, control_points, title="Bézier Curve"):
    """
    Plots the Bézier curve, its control points, and the control polygon.
    """
    control_points = np.array(control_points)
    
    plt.figure(figsize=(10, 8))
    
    # Plot the Bézier curve itself
    plt.plot(curve[:, 0], curve[:, 1], 'b-', lw=2, label='Bézier Curve')
    
    # Plot the control polygon (lines connecting control points)
    plt.plot(control_points[:, 0], control_points[:, 1], 'ro--', 
             label='Control Polygon')
             
    # Plot the control points
    plt.plot(control_points[:, 0], control_points[:, 1], 'go', 
             markersize=10, label='Control Points')
    
    # Annotate control points for clarity
    for i, (x, y) in enumerate(control_points):
        plt.text(x + 5, y, f'P{i}', fontsize=14, verticalalignment='bottom')

    plt.title(title, fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# --- Main Execution ---
if __name__ == '__main__':
    # --- Example 1: Cubic Bézier Curve ---
    # Define the control points for a classic "S" curve
    cubic_control_points = [
        (10, 10),    # P0: Start point
        (20, 150),   # P1: Control point
        (180, 150),  # P2: Control point
        (200, 20)    # P3: End point
    ]
    
    # Generate the curve's points
    cubic_curve = bezier_curve(cubic_control_points)
    
    # Plot the curve and its controls
    plot_curve_with_controls(cubic_curve, cubic_control_points, 
                             title="Cubic Bézier Curve")

    # --- Example 2: Quadratic Bézier Curve (an arc) ---
    quadratic_control_points = [
        (50, 250),   # P0
        (150, 50),   # P1
        (250, 250),   # P2
        (350, 350),   # P0
        (0, 650),   # P1
        (550, 750)
    ]
    quadratic_curve = bezier_curve(quadratic_control_points)
    plot_curve_with_controls(quadratic_curve, quadratic_control_points, 
                             title="Quadratic Bézier Curve")