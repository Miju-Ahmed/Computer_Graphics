import numpy as np
import matplotlib.pyplot as plt

def is_inside(p, edge_start, edge_end):
    """Return True if point p is on the 'inside' side of the directed edge (edge_start -> edge_end).
    We define 'inside' as the left side of the edge (counter-clockwise clip polygon)."""
    # Compute cross product (edge_end - edge_start) x (p - edge_start)
    return ((edge_end[0] - edge_start[0]) * (p[1] - edge_start[1]) -
            (edge_end[1] - edge_start[1]) * (p[0] - edge_start[0])) >= 0

def compute_intersection(s, e, cp1, cp2):
    """Compute intersection of line segment (s->e) with infinite line (cp1->cp2).
    Returns intersection point (x,y). Assumes the lines are not parallel for cases where intersection is needed."""
    # Line 1: s + t*(e - s)
    # Line 2: cp1 + u*(cp2 - cp1)
    x1, y1 = s
    x2, y2 = e
    x3, y3 = cp1
    x4, y4 = cp2

    denom = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if abs(denom) < 1e-10:
        # Lines are parallel; return end point or midpoint as fallback
        return ((e[0] + s[0]) / 2.0, (e[1] + s[1]) / 2.0)

    px = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denom
    py = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denom
    return (px, py)

def sutherland_hodgman(subject_polygon, clip_polygon):
    """Clip a polygon (subject_polygon) by a convex polygon (clip_polygon).
    subject_polygon & clip_polygon are lists of (x,y) tuples. clip_polygon should be ccw (counter-clockwise)."""
    output_list = subject_polygon[:]
    cp_count = len(clip_polygon)

    for i in range(cp_count):
        input_list = output_list
        if not input_list:
            break  # fully clipped
        output_list = []

        cp1 = clip_polygon[i]
        cp2 = clip_polygon[(i + 1) % cp_count]

        s = input_list[-1]  # start with last vertex (previous vertex)
        for e in input_list:
            if is_inside(e, cp1, cp2):
                if is_inside(s, cp1, cp2):
                    # Case: s inside, e inside -> output e
                    output_list.append(e)
                else:
                    # Case: s outside, e inside -> output intersection then e
                    inter = compute_intersection(s, e, cp1, cp2)
                    output_list.append(inter)
                    output_list.append(e)
            else:
                if is_inside(s, cp1, cp2):
                    # Case: s inside, e outside -> output intersection
                    inter = compute_intersection(s, e, cp1, cp2)
                    output_list.append(inter)
                else:
                    # s outside, e outside -> output nothing
                    pass
            s = e  # advance

    return output_list

# -------------------------
# Example usage & plotting
# -------------------------
if __name__ == "__main__":
    # Subject polygon (possibly nonconvex)
    subject = [
        (1, 1), (5, 2), (6, 5), (4, 6), (2, 5), (0.5, 3)
    ]

    # Clipping polygon: axis-aligned rectangle (counter-clockwise)
    # rectangle with corners (xmin, ymin) = (2, 1.5) and (xmax, ymax) = (5, 5)
    clip_rect = [
        (2, 1.5),
        (5, 1.5),
        (5, 5),
        (2, 5)
    ]

    clipped = sutherland_hodgman(subject, clip_rect)

    # Plot subject polygon
    subj_np = np.array(subject + [subject[0]])
    plt.plot(subj_np[:,0], subj_np[:,1], '-o', label='Subject polygon', color='tab:blue')

    # Plot clip polygon (rectangle)
    clip_np = np.array(clip_rect + [clip_rect[0]])
    plt.plot(clip_np[:,0], clip_np[:,1], '-o', label='Clip polygon', color='tab:orange')

    # Plot clipped polygon
    if clipped:
        clipres_np = np.array(clipped + [clipped[0]])
        plt.fill(clipres_np[:,0], clipres_np[:,1], alpha=0.3, label='Clipped polygon', color='tab:green')
        plt.plot(clipres_np[:,0], clipres_np[:,1], '-s', color='tab:green')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.title('Sutherland–Hodgman Polygon Clipping Example')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()
