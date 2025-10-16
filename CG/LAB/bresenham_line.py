from PIL import Image
import matplotlib.pyplot as plt

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    err = dx - dy
    x, y = x0, y0

    while True:
        points.append((x, y))
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return points


# --- Create a white canvas ---
w, h = 500, 500
img = Image.new('RGB', (w, h), "white")
px = img.load()

# --- Draw a -45° line ---
# Example: start lower-left and go to upper-right
# Δx = 400, Δy = -400  → slope = -1 (−45°)
lines = [(50, 450, 450, 50)]

for (x0, y0, x1, y1) in lines:
    for x, y in bresenham_line(x0, y0, x1, y1):
        if 0 <= x < w and 0 <= y < h:
            px[x, y] = (0, 0, 0)

# --- Save and display ---
img.save("bresenham_-45deg.png")

plt.imshow(img)
plt.title("Bresenham −45° Line Drawing")
plt.axis("off")
plt.show()
