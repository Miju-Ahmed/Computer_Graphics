import matplotlib.pyplot as plt

def Bresenham_Line(x1,y1,x2,y2):
    points=[]
    dx=abs(x1-x2)
    dy=-abs(y1-y2)
    sx=1 if x1<x2 else -1
    sy=1 if y1<y2 else -1
    err=dx+dy
    x,y=x1,y1
    while True:
        points.append((x,y))
        if x==x2 and y==y2:
            break
        e2=2*err
        if e2>=dy:
            err+=dy
            x+=sx
        if e2<=sx:
            err+=dx
            y+=sy
    return points

if __name__=="__main__":
    x1, y1 = 2, 2
    x2, y2 = 15, 8
    line_pixels = Bresenham_Line(x1, y1, x2, y2)

    xs, ys = zip(*line_pixels)
    plt.figure(figsize=(6, 6))
    plt.scatter(xs, ys, c='red', s=100, marker='s')  
    plt.grid(True, which='both')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Bresenham Line Drawing Algorithm")
    plt.show()