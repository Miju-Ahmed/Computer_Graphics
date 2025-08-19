import numpy as np
import matplotlib.pyplot as plt

def is_inside(p,edge_start,edge_end):
    return ((edge_end[0]-edge_start[0])*(p[1]-edge_start[1])-
            (edge_end[1]-edge_start[1])*(p[0]-edge_start[1]))>=0
def compute_intersection(s,e,cp1,cp2):
    x1,y1=s
    x2,y2=e
    x3,y3=cp1
    x4,y4=cp2
    denom=(x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
    if abs(denom)<1e-10:
        return ((e[0]+s[0])/2.0,(e[1]+s[1])/2.0)
    