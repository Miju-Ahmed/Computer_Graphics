import matplotlib.pyplot as plt
import matplotlib.patches as patches

ins = 0
le = 1
ri = 2
bo = 4
to = 8

def compute_outcode(x,y,xmin,ymin,xmax,ymax):
    code = ins
    