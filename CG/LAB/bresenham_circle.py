import matplotlib.pyplot as plt

def plot_circle(xc,yc,x,y,points):
    points.extend([
        (xc+x, yc+y),
        (xc+x, yc-y),
        (xc-x, yc+y),
        (xc-x, yc-y),
        (xc+y, yc+x),
        (xc-y, yc+x),
        (xc+y, yc-x),
        (xc-y, yc-x)
    ])
def bresenham_circle(xc,yc,r):
    x,y=0,r
    d = 3-2*r
    points = []
    while x<=y:
        plot_circle(xc, yc, x, y, points)
        if d<0:
            d = d+4*x +6
        else:
            d = d+4*(x-y) + 10
            y = y-1
        x += 1
    return points

xc,yc,r = -10, 34, 50
circle_points = bresenham_circle(xc,yc,r)
x_vals, y_vals = zip(*circle_points)
plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='red', s=10)
plt.gca().set_aspect('equal', 'box')
plt.grid(True)
plt.show()