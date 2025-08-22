import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Define constants for clipping edges
LEFT_EDGE = 0
RIGHT_EDGE = 1
BOTTOM_EDGE = 2
TOP_EDGE = 3

def is_inside(p, edge, clip_window):
    """Checks if a point p is 'inside' a given clipping edge."""
    x, y = p
    x_min, y_min, x_max, y_max = clip_window
    if edge == LEFT_EDGE:
        return x >= x_min
    elif edge == RIGHT_EDGE:
        return x <= x_max
    elif edge == BOTTOM_EDGE:
        return y >= y_min
    elif edge == TOP_EDGE:
        return y <= y_max
    return False

def get_intersection(p1, p2, edge, clip_window):
    """Calculates the intersection of a line segment p1-p2 with a clipping edge."""
    x1, y1 = p1
    x2, y2 = p2
    x_min, y_min, x_max, y_max = clip_window
    
    # Avoid division by zero
    dx = x2 - x1
    dy = y2 - y1

    if edge == LEFT_EDGE:
        # y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
        return (x_min, y1 + dy * (x_min - x1) / dx if dx != 0 else y1)
    elif edge == RIGHT_EDGE:
        # y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
        return (x_max, y1 + dy * (x_max - x1) / dx if dx != 0 else y1)
    elif edge == BOTTOM_EDGE:
        # x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
        return (x1 + dx * (y_min - y1) / dy if dy != 0 else x1, y_min)
    elif edge == TOP_EDGE:
        # x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
        return (x1 + dx * (y_max - y1) / dy if dy != 0 else x1, y_max)

def clip_polygon_against_edge(subject_polygon, edge, clip_window):
    """Clips a polygon against a single edge of the clipping window."""
    output_polygon = []
    
    # Use the first vertex as the starting point
    s = subject_polygon[-1]
    
    for p in subject_polygon:
        # Case 1: Both points are inside
        if is_inside(p, edge, clip_window):
            if not is_inside(s, edge, clip_window):
                # S is outside, P is inside: Add intersection and P
                intersection = get_intersection(s, p, edge, clip_window)
                output_polygon.append(intersection)
            output_polygon.append(p)
        # Case 2: S is inside, P is outside
        elif is_inside(s, edge, clip_window):
            # Add intersection only
            intersection = get_intersection(s, p, edge, clip_window)
            output_polygon.append(intersection)
        # Case 3: Both points are outside - do nothing
        
        # Update s for the next iteration
        s = p
        
    return output_polygon

def sutherland_hodgman_clip(subject_polygon, clip_window):
    """
    Clips a polygon using the Sutherland-Hodgman algorithm.
    
    Args:
        subject_polygon (list of tuples): The vertices of the polygon to be clipped, e.g., [(x1, y1), ...].
        clip_window (tuple): The clipping rectangle (x_min, y_min, x_max, y_max).
        
    Returns:
        list of tuples: The vertices of the clipped polygon.
    """
    clipped = list(subject_polygon)
    
    # Clip against each of the four edges
    for edge in range(4):
        if not clipped:
            break
        clipped = clip_polygon_against_edge(clipped, edge, clip_window)
        
    return clipped

def plot_polygons(subject_polygon, clip_window, clipped_polygon):
    """Plots the original, clipping, and clipped polygons."""
    fig, ax = plt.subplots()

    # Original Polygon
    poly_orig = patches.Polygon(subject_polygon, closed=True, edgecolor='blue', facecolor='none', linestyle='--', linewidth=2, label='Original Polygon')
    ax.add_patch(poly_orig)

    # Clipping Window
    x_min, y_min, x_max, y_max = clip_window
    rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                             linewidth=2, edgecolor='red', facecolor='none', linestyle=':', label='Clipping Window')
    ax.add_patch(rect)

    # Clipped Polygon
    if clipped_polygon:
        poly_clipped = patches.Polygon(clipped_polygon, closed=True, edgecolor='green', facecolor='green', alpha=0.4, label='Clipped Polygon')
        ax.add_patch(poly_clipped)

    # Set up plot
    ax.set_title("Sutherland-Hodgman Polygon Clipping")
    ax.legend()
    ax.set_aspect('equal', 'box')
    
    # Set plot limits to see all polygons clearly
    all_points = subject_polygon + list(zip(*[iter([x_min, y_min, x_max, y_max])]*2))
    all_x = [p[0] for p in all_points]
    all_y = [p[1] for p in all_points]
    plt.xlim(min(all_x) - 10, max(all_x) + 10)
    plt.ylim(min(all_y) - 10, max(all_y) + 10)
    
    plt.grid(True)
    plt.show()

# --- Example Usage ---
if __name__ == "__main__":
    # 1. Define the polygon to be clipped (a triangle)
    subject_polygon = [(50, 150), (200, 50), (350, 150),(200,250)]
    
    # 2. Define the clipping window
    clip_window = (100, 100, 300, 200) # (x_min, y_min, x_max, y_max)
    
    # 3. Perform the clipping
    clipped_polygon = sutherland_hodgman_clip(subject_polygon, clip_window)
    
    # 4. Print results and plot
    print("Original Polygon Vertices:", subject_polygon)
    print("Clipped Polygon Vertices:", clipped_polygon)
    
    plot_polygons(subject_polygon, clip_window, clipped_polygon)