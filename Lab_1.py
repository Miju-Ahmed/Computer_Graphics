import numpy as np
import matplotlib.pyplot as plt

WIDTH, HEIGHT = 400, 300
BACKGROUND_COLOR = (0.8, 0.8, 0.8)  

frame_buffer = np.full((HEIGHT, WIDTH, 3), BACKGROUND_COLOR)
# Depth buffer to store the z-coordinate of the closest object at each pixel
depth_buffer = np.full((HEIGHT, WIDTH), np.inf)

# --- Scene Definition (Triangles) ---
# Each triangle is defined by its 3 vertices (x, y, z) and a color
triangles = [
    {
        'vertices': np.array([[100, 250, -10], [200, 50, -10], [300, 250, -10]]),
        'color': (1, 0, 0)  # Red
    },
    {
        'vertices': np.array([[150, 200, -5], [250, 200, -5], [200, 100, -5]]),
        'color': (0, 1, 0)  # Green
    },
    {
        'vertices': np.array([[50, 150, -15], [350, 150, -15], [200, 280, -2]]),
        'color': (0, 0, 1)  # Blue
    }
]

# --- Z-Buffer Algorithm Implementation ---
def z_buffer_render(triangles):
    """
    Renders the given triangles using the Z-buffer algorithm.
    """
    for triangle in triangles:
        verts = triangle['vertices']
        color = triangle['color']

        # Bounding box for the triangle
        min_x = max(0, int(np.min(verts[:, 0])))
        max_x = min(WIDTH - 1, int(np.max(verts[:, 0])))
        min_y = max(0, int(np.min(verts[:, 1])))
        max_y = min(HEIGHT - 1, int(np.max(verts[:, 1])))

        # Rasterize the triangle
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                # Barycentric coordinates to check if the pixel is inside the triangle
                # and to interpolate the depth
                p = np.array([x, y])
                v0, v1, v2 = verts[:, :2]
                w0 = ((v1[1] - v2[1]) * (p[0] - v2[0]) + (v2[0] - v1[0]) * (p[1] - v2[1])) / \
                     ((v1[1] - v2[1]) * (v0[0] - v2[0]) + (v2[0] - v1[0]) * (v0[1] - v2[1]))
                w1 = ((v2[1] - v0[1]) * (p[0] - v2[0]) + (v0[0] - v2[0]) * (p[1] - v2[1])) / \
                     ((v1[1] - v2[1]) * (v0[0] - v2[0]) + (v2[0] - v1[0]) * (v0[1] - v2[1]))
                w2 = 1.0 - w0 - w1

                if w0 >= 0 and w1 >= 0 and w2 >= 0:
                    # Interpolate depth
                    z = w0 * verts[0, 2] + w1 * verts[1, 2] + w2 * verts[2, 2]

                    # Depth test
                    if z < depth_buffer[y, x]:
                        depth_buffer[y, x] = z
                        frame_buffer[y, x] = color

# --- Main Execution ---
if __name__ == '__main__':
    z_buffer_render(triangles)

    plt.imshow(frame_buffer)
    plt.title('Z-Buffer Hidden Surface Elimination')
    plt.axis('off')
    plt.show()