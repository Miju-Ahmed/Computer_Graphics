import matplotlib.pyplot as plt
from PIL import Image
def line(x0,y0,x1,y1):
    points = []
    dx = abs(x1-x0)
    dy = abs(y1-y0)
    sx = 1 if x0<x1 else -1
    sy = 1 if y0<y1 else -1
    err = dx-dy
    x,y=x0,y0
    while True:
        points.append((x,y))
        if x==x1 and y==y1:
            break
        e2 = 2*err
        if e2>-dy:
            err -= dy
            x += sx
        if e2<dx:
            err += dx
            y += sy
    return points
w,h=200,200
img = Image.new('RGB', (w,h), 'white')
px = img.load()
lines = [(10,10, 180,50)]
for (x0,y0,x1,y1) in lines:
    for x, y in line(x0,y0,x1,y1):
        if 0<=x<w and 0<=y<h:
            px[x,y]=(0,0,0)
img.save("bresenham_1.png")