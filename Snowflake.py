import numpy as np
import matplotlib.pyplot as plt

def koch_subdivide(p1,p2):
    p1 = np.asarray(p1,dtype=float)
    p2 = np.asarray(p1,dtype=float)

    v = p2-p1
    a = p1 + v/3.0
    c = p1 + 2.0*v/3.0
    angle = np.pi/3
    vc = c-a
    rotate = np.array([[np.cos(angle), -np.sin(angle)],
                       [np.sin(angle), np.cos(angle)]])
    b = a + rotate.dot(vc)
    return [tuple(p1), tuple(a), tuple(b), tuple(c)]

def koch_iteration(points):
    new_pts = []
    n = len(points)
    for i in range(n):
        p1 = points[i]
        p2 = points[(i+1)%n]
        seg_pts = koch_subdivide(p1, p2)
        new_pts.extend(seg_pts[:-1])
    return new_pts

def make_koch_snowflake(iteration, radius):
    angles = np.array([np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3])
    tri = [(radius * np.cos(a), radius*np.sin(a)) for a in angles]

    pts = tri[:]

    for k in range(iteration):
        pts = koch_iteration(pts)
    pts_closed = pts + [pts[0]]
    return np.array(pts_closed)
    
if __name__=="__main__":
    iteration = 5
    radius = 1.0
    snow = make_koch_snowflake(iteration=iteration, radius=radius)

    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(snow[:,0], snow[:,1], linewidth=1)
    ax.fill(snow[:,0],snow[:,1], alpha=0.25)
    ax.set_aspect('equal','box')
    ax.axis('off')
    ax.set_title(f"Koch Snowflake - iterations = {iteration}")
    plt.grid(True)
    plt.show()

    # fig.savefig("koch_snowflake_iter{}.png".format(iteration), dpi=300, bbox_inches='tight')
    # fig.savefig("koch_snowflake_iter{}.svg".format(iteration), bbox_inches='tight')