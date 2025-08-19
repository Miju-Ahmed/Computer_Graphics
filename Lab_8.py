import numpy as np
import matplotlib.pyplot as plt

def koch_subdivide(p1, p2):
    """Given endpoints p1, p2 (arrays), return list of 4 points that replace the segment:
       p1, a, b, c where:
         a = p1 + (p2-p1)/3
         c = p1 + 2*(p2-p1)/3
         b = a rotated 60 degrees around a towards c to form the equilateral bump."""
    p1 = np.asarray(p1, dtype=float)
    p2 = np.asarray(p2, dtype=float)
    v = p2 - p1
    a = p1 + v / 3.0
    c = p1 + 2.0 * v / 3.0

    # rotate vector (c - a) by +90? No — rotate by +60 degrees for outward bump:
    angle = np.pi / 3.0  # 60 degrees
    # vector from a to c
    vc = c - a
    # rotate vc by +60 degrees
    rot = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle),  np.cos(angle)]])
    b = a + rot.dot(vc)

    return [tuple(p1), tuple(a), tuple(b), tuple(c)]

def koch_iteration(points):
    """Perform one iteration of Koch subdivision on the polygon defined by points (closed)."""
    new_pts = []
    n = len(points)
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        seg_pts = koch_subdivide(p1, p2)
        # append all but the last point (it will be start of next segment)
        new_pts.extend(seg_pts[:-1])
    return new_pts

def make_koch_snowflake(iterations=4, radius=1.0):
    """Create coordinates of Koch snowflake after given iterations.
       Start from equilateral triangle of circumradius 'radius' centered at origin."""
    # Create equilateral triangle vertices (ccw)
    angles = np.array([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3])
    tri = [(radius * np.cos(a), radius * np.sin(a)) for a in angles]

    pts = tri[:]  # closed polygon (we treat it cyclically)
    for k in range(iterations):
        pts = koch_iteration(pts)
    # close polygon by appending first point (useful for plotting fills)
    pts_closed = pts + [pts[0]]
    return np.array(pts_closed)

if __name__ == "__main__":
    # Parameters
    iterations = 5   # try 0..6 (>=6 becomes heavy)
    radius = 1.0

    snow = make_koch_snowflake(iterations=iterations, radius=radius)

    # Plot
    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(snow[:,0], snow[:,1], linewidth=1)
    ax.fill(snow[:,0], snow[:,1], alpha=0.25)
    ax.set_aspect('equal', 'box')
    ax.axis('off')
    ax.set_title(f'Koch Snowflake — iterations={iterations}')
    plt.show()

    # Optionally save:
    # fig.savefig("koch_snowflake_iter{}.png".format(iterations), dpi=300, bbox_inches='tight')
    # fig.savefig("koch_snowflake_iter{}.svg".format(iterations), bbox_inches='tight')
