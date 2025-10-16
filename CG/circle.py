import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
    points.extend([
        (xc+x, yc+y),
        (xc-x, yc+y),
        (xc+x, yc-y),
        (xc-x, yc-y),
        (xc+y, yc+x),
        (xc-y, yc+x),
        (xc+y, yc-x),
        (xc-y, yc-x)
    ])

def bresenham_circle(xc, yc, r):
    x, y = 0, r
    d = 3-3*r
    points = []
    while x<=y:
        plot_circle_points(xc, yc, x, y, points)
        if d<0:
            d = d + 4*x + 6
        else:
            d = d + 4*(x-y) + 10
            y = y - 1
        x = x+1
    return points
if __name__ =="__main__":
    xc, yc, r = -20, 10, 15
    circle_points = bresenham_circle(xc, yc, r)
    x_vals, yc_vals = zip(*circle_points)
    plt.figure(figsize=(10,10))
    plt.scatter(x_vals, yc_vals)
    plt.gca().set_aspect('equal', adjustable = 'box')
    plt.grid(True)
    plt.show()