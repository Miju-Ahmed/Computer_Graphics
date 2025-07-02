import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Initial polygon and clip window
polygon = [
    (50, 150), (200, 50), (350, 150), (350, 300),
    (250, 300), (200, 250), (150, 350), (100, 250), (100, 200)
]

clip_window = (100, 100, 300, 300)
x_min, y_min, x_max, y_max = clip_window

edges = ['Left', 'Top', 'Right', 'Bottom']

def inside(p, edge_name):
    x, y = p
    if edge_name == 'Left':
        return x >= x_min
    elif edge_name == 'Right':
        return x <= x_max
    elif edge_name == 'Top':
        return y <= y_max
    elif edge_name == 'Bottom':
        return y >= y_min

def intersect(p1, p2, edge_name):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2: m = float('inf')
    else: m = (y2 - y1) / (x2 - x1)
    
    if edge_name == 'Left':
        x = x_min
        y = y1 + m * (x - x1)
    elif edge_name == 'Right':
        x = x_max
        y = y1 + m * (x - x1)
    elif edge_name == 'Top':
        y = y_max
        x = x1 if m == float('inf') else x1 + (y - y1) / m
    elif edge_name == 'Bottom':
        y = y_min
        x = x1 if m == float('inf') else x1 + (y - y1) / m
    return (x, y)

def clip_edge(polygon, edge_name):
    output = []
    for i in range(len(polygon)):
        curr = polygon[i]
        prev = polygon[i - 1]
        curr_in = inside(curr, edge_name)
        prev_in = inside(prev, edge_name)

        if curr_in:
            if not prev_in:
                output.append(intersect(prev, curr, edge_name))
            output.append(curr)
        elif prev_in:
            output.append(intersect(prev, curr, edge_name))
    return output

# Precompute frames (original + after each edge)
frames = [polygon]
for edge in edges:
    next_poly = clip_edge(frames[-1], edge)
    frames.append(next_poly)

# Set up plot
fig, ax = plt.subplots()
ax.set_title("Sutherland–Hodgman Polygon Clipping Animation")
ax.set_xlim(0, 400)
ax.set_ylim(0, 400)
ax.set_aspect('equal')
ax.grid(True)

# Draw clip window
clip_rect, = ax.plot(
    [x_min, x_max, x_max, x_min, x_min],
    [y_min, y_min, y_max, y_max, y_min],
    'g--', label="Clip Window"
)

# Initialize polygon line
poly_line, = ax.plot([], [], 'bo-', label="Clipped Polygon")
text = ax.text(10, 10, "", fontsize=12)

def update(frame_num):
    poly = frames[frame_num]
    x = [p[0] for p in poly] + [poly[0][0]]
    y = [p[1] for p in poly] + [poly[0][1]]
    poly_line.set_data(x, y)
    if frame_num == 0:
        text.set_text("Step 0: Original Polygon")
    else:
        text.set_text(f"Step {frame_num}: Clipped with {edges[frame_num - 1]} edge")
    return poly_line, text

ani = animation.FuncAnimation(fig, update, frames=len(frames),
                              interval=1500, repeat=False, blit=False)

plt.legend()
plt.show()
