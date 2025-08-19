# import numpy as np
# import matplotlib
# # Use TkAgg to avoid Qt cleanup error
# matplotlib.use("TkAgg")
# import matplotlib.pyplot as plt
# from matplotlib import animation
# from matplotlib.collections import PatchCollection
# from matplotlib.patches import Rectangle

# # -----------------------------
# # Bresenham / Midpoint Circle Algorithm
# # -----------------------------
# def bresenham_circle_points(xc, yc, r):
#     points = []
#     x = 0
#     y = r
#     d = 3 - 2 * r

#     while y >= x:
#         # 8-way symmetry
#         points.extend([
#             (xc + x, yc + y),
#             (xc - x, yc + y),
#             (xc + x, yc - y),
#             (xc - x, yc - y),
#             (xc + y, yc + x),
#             (xc - y, yc + x),
#             (xc + y, yc - x),
#             (xc - y, yc - x)
#         ])
#         if d < 0:
#             d = d + 4 * x + 6
#         else:
#             d = d + 4 * (x - y) + 10
#             y -= 1
#         x += 1
#     # Remove duplicates
#     points = list(dict.fromkeys(points))
#     return points

# # -----------------------------
# # Example circle center & radius
# # -----------------------------
# xc, yc = 10, 10
# radius = 8

# points = bresenham_circle_points(xc, yc, radius)

# # -----------------------------
# # Grid Setup
# # -----------------------------
# min_x = xc - radius - 2
# max_x = xc + radius + 2
# min_y = yc - radius - 2
# max_y = yc + radius + 2

# fig, ax = plt.subplots(figsize=(7, 7))
# ax.set_xlim(min_x - 0.5, max_x + 0.5)
# ax.set_ylim(min_y - 0.5, max_y + 0.5)
# ax.set_aspect('equal', 'box')
# ax.invert_yaxis()
# ax.set_xticks(range(min_x, max_x + 1))
# ax.set_yticks(range(min_y, max_y + 1))
# ax.grid(True, linewidth=0.5)

# # Draw empty grid squares
# patches = []
# for gx in range(min_x, max_x + 1):
#     for gy in range(min_y, max_y + 1):
#         rect = Rectangle((gx - 0.5, gy - 0.5), 1, 1, fill=False, linewidth=0)
#         patches.append(rect)
# pc = PatchCollection(patches, match_original=True)
# ax.add_collection(pc)

# # -----------------------------
# # Animation Objects
# # -----------------------------
# visited_scatter = ax.scatter([], [], s=300, color='blue')
# current_scatter = ax.scatter([], [], s=500, marker='s', color='red')
# center_scatter = ax.scatter([xc], [yc], s=200, marker='X', color='green')
# title = ax.text(0.02, 1.02, '', transform=ax.transAxes)

# # -----------------------------
# # Animation Functions
# # -----------------------------
# def init():
#     visited_scatter.set_offsets(np.empty((0, 2)))
#     current_scatter.set_offsets(np.empty((0, 2)))
#     title.set_text('')
#     return visited_scatter, current_scatter, title

# def animate(i):
#     if i < len(points):
#         visited = np.array(points[:i+1])
#         current = np.array([points[i]])
#     else:
#         visited = np.array(points)
#         current = np.array([points[-1]])
#     visited_scatter.set_offsets(visited.reshape(-1, 2))
#     current_scatter.set_offsets(current.reshape(-1, 2))
#     title.set_text(f'Step {min(i+1, len(points))} / {len(points)} — point = {tuple(current[0])}')
#     return visited_scatter, current_scatter, title

# # -----------------------------
# # Run Animation (no blit)
# # -----------------------------
# anim = animation.FuncAnimation(
#     fig, animate, init_func=init,
#     frames=len(points) + 10, interval=300, blit=False, repeat=False
# )

# plt.show()



import matplotlib.pyplot as plt

def plot_circle_points(xc, yc, x, y, points):
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

def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r
    points = []

    while x <= y:
        plot_circle_points(xc, yc, x, y, points)
        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1
        x += 1

    return points

# Example usage
xc, yc, r = 50, 50, 30
circle_points = bresenham_circle(xc, yc, r)

# Plot
x_vals, y_vals = zip(*circle_points)
plt.figure(figsize=(6,6))
plt.scatter(x_vals, y_vals, color='blue', s=10)
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(True)
plt.show()
