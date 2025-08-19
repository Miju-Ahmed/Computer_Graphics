import matplotlib.pyplot as plt

def plot_circle_points(xc,yc,x,y,points):
    points.extend([
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ])

def Bresenham_circle(xc,yc,r):
    x=0
    y=r
    d=3-2*r
    points=[]
    while x<=y:
        plot_circle_points(xc,yc,x,y,points)
        if d<0:
            d=d+4*x+6
        else:
            d=d+4*(x-y)+10
            y=y-1
        x+=1
    return points
if __name__=="__main__":
    xc,yc,r=-10,34,50
    circle_points=Bresenham_circle(xc,yc,r)
    x_vals,y_vals=zip(*circle_points)
    plt.figure(figsize=(6,6))
    plt.scatter(x_vals, y_vals, color='blue', s=10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()
