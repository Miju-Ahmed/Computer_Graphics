# bresenham_circle.py
import matplotlib.pyplot as plt

def bresenham_circle(xc, yc, r):
    """Return list of (x,y) points for a circle centered at (xc,yc) with radius r."""
    x = 0
    y = r
    d = 3 - 2 * r
    points = []

    while x <= y:
        # All 8 symmetric points
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x),
        ])
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points


if __name__ == "__main__":
    xc, yc, r = 100, 100, 60
    circle_points = bresenham_circle(xc, yc, r)

    # Plot the circle
    xs, ys = zip(*circle_points)
    plt.scatter(xs, ys, s=10, color="blue")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.title("Bresenham Circle Drawing")
    plt.show()
