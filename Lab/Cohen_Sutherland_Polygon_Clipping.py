import matplotlib.pyplot as plt
import matplotlib.patches as patches

LEFT = 0
RIGHT = 1
BOTTOM = 2
TOP = 3

def is_inside(p, edge, clip_value):
    x, y = p
    if edge == LEFT:
        return x >= clip_value
    elif edge == RIGHT:
        return x <= clip_value
    elif edge == BOTTOM:
        return y >= clip_value
    elif edge == TOP:
        return y <= clip_value
    return False

def get_intersection(p1, p2, edge, clip_value):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1

    if edge == LEFT or edge == RIGHT:
        if dx == 0:
            return (clip_value, y1)
        y = y1 + dy * (clip_value - x1) / dx
        return (clip_value, y)

    elif edge == BOTTOM or edge == TOP:
        if dy == 0:
            return (x1, clip_value)
        x = x1 + dx * (clip_value - y1) / dy
        return (x, clip_value)

def clip_polygon_against_edge(polygon, edge, clip_value):
    output_polygon = []
    if not polygon:
        return output_polygon

    s = polygon[-1]  

    for p in polygon:
        s_inside = is_inside(s, edge, clip_value)
        p_inside = is_inside(p, edge, clip_value)

        # Case 1: Both points are inside -> Add the second point
        if s_inside and p_inside:
            output_polygon.append(p)
        # Case 2: S is inside, P is outside -> Add intersection only
        elif s_inside and not p_inside:
            intersection = get_intersection(s, p, edge, clip_value)
            output_polygon.append(intersection)
        # Case 3: S is outside, P is inside -> Add intersection AND the second point
        elif not s_inside and p_inside:
            intersection = get_intersection(s, p, edge, clip_value)
            output_polygon.append(intersection)
            output_polygon.append(p)
        # Case 4: Both points are outside -> Do nothing

        s = p  # Move to the next edge
    return output_polygon

def sutherland_hodgman_polygon_clip(polygon, clip_window):
    x_min, y_min, x_max, y_max = clip_window
    
    clipped = clip_polygon_against_edge(polygon, LEFT, x_min)
    clipped = clip_polygon_against_edge(clipped, RIGHT, x_max)
    clipped = clip_polygon_against_edge(clipped, BOTTOM, y_min)
    clipped = clip_polygon_against_edge(clipped, TOP, y_max)
    
    return clipped

def plot_polygons(polygon, window, clipped):
    fig, ax = plt.subplots()

    poly_org = patches.Polygon(polygon, closed=True, edgecolor='red', facecolor='none', linestyle='--', linewidth=2, label='Original Polygon')
    ax.add_patch(poly_org)

    x_min, y_min, x_max, y_max = window
    rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                             linewidth=2, facecolor='none', edgecolor='green', linestyle=':', label='Clipping Window')
    ax.add_patch(rect)

    if clipped:
        poly_clipped = patches.Polygon(clipped, closed=True, edgecolor='blue', linewidth=2, facecolor='blue', alpha=0.4, label='Clipped Polygon')
        ax.add_patch(poly_clipped)

    ax.set_title("Sutherland-Hodgman Polygon Clipping")
    ax.legend()
    ax.set_aspect('equal', 'box')

    all_points = polygon + [(x_min, y_min), (x_max, y_max)]
    all_x = [p[0] for p in all_points]
    all_y = [p[1] for p in all_points]
    plt.xlim(min(all_x) - 20, max(all_x) + 20)
    plt.ylim(min(all_y) - 20, max(all_y) + 20)
    
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    subject_polygon = [(50, 150), (200, 50), (350, 150), (100, 250), (200,150)]
    clip_window = (100, 100, 300, 200)

    clipped_polygon = sutherland_hodgman_polygon_clip(subject_polygon, clip_window)

    print("Original Polygon Vertices:", subject_polygon)
    print("Clipped Polygon Vertices:", clipped_polygon)

    plot_polygons(subject_polygon, clip_window, clipped_polygon)