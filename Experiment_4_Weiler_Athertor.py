import matplotlib.pyplot as plt
import matplotlib.animation as animation
from shapely.geometry import Polygon

# ----- SUBJECT POLYGON (concave) -----
subject = Polygon([
    (100, 150), (200, 50), (300, 150), (250, 250), (150, 250), (180, 180)
])

# ----- CLIPPING WINDOW (rectangular) -----
clip_rect = Polygon([
    (150, 100), (350, 100), (350, 300), (150, 300)
])

# ----- COMPUTE CLIPPED POLYGON USING SHAPELY -----
clipped = subject.intersection(clip_rect)

# ----- PREPARE FIGURE -----
fig, ax = plt.subplots()
ax.set_xlim(50, 400)
ax.set_ylim(0, 350)
ax.set_aspect('equal')
ax.set_title("Weiler–Atherton Clipping (Live)")

subject_patch, = ax.plot([], [], 'b-', label='Subject Polygon')
clip_patch, = ax.plot([], [], 'g--', label='Clipping Window')
clipped_patch, = ax.plot([], [], 'r-', label='Clipped Result')
text = ax.text(50, 330, "", fontsize=12)

# ----- Convert polygon to x/y -----
def get_coords(poly):
    x, y = poly.exterior.xy
    return list(x), list(y)

# ----- ANIMATION FRAMES -----
def animate(i):
    if i == 0:
        x, y = get_coords(subject)
        subject_patch.set_data(x, y)
        clip_patch.set_data([], [])
        clipped_patch.set_data([], [])
        text.set_text("Step 1: Subject Polygon")
    elif i == 1:
        x, y = get_coords(clip_rect)
        clip_patch.set_data(x, y)
        text.set_text("Step 2: Clipping Window")
    elif i == 2:
        if clipped.is_empty:
            text.set_text("No intersection found.")
        else:
            x, y = get_coords(clipped)
            clipped_patch.set_data(x, y)
            text.set_text("Step 3: Clipped Polygon")
    return subject_patch, clip_patch, clipped_patch, text

ani = animation.FuncAnimation(
    fig, animate, frames=3, interval=1500, repeat=False
)

plt.legend()
plt.grid(True)
plt.show()
