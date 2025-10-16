import matplotlib.pyplot as plt
import matplotlib.patches as patches

inside,left,right,top,bottom=0,1,2,4,8

def compute_outcode(x,y,xmin,ymin,xmax,ymax):
    code = inside
    if x<xmin:
        code|=left
    elif x>xmax:
        code|=right
    elif y<ymin:
        code |= bottom
    elif y>ymax:
        code|=top
    return code
def cohen_suth(x1,y1,x2,y2,xmin,ymin,xmax,ymax):
    o1 = compute_outcode(x1,y1,xmin,ymin, xmax, ymax)
    o2 = compute_outcode(x2,y2, xmin,ymin,xmax, ymax)
    accepted = True
    while True:
        if not(o1|o2):
            accepted=True
            break
        elif (o1&o2):
            break
        else:
            out = o1 if o1 else o2
            if out&bottom:
                x = x1+(x2-x1)*(ymin-y1)/(y2-y1)
                y = ymin
            elif out&top:
                x = x1 + (x2-x1)*(ymax-y1)/(y2-y1)
                y = ymax
            elif out&left:
                y = y1 + (y2-y1)*(xmin-x1)/(x2-x1)
                x = xmin
            elif out&right:
                y = y1 + (y2-y1)*(xmax-x1)/(x2-x1)
                x = xmax
            if out==o1:
                x1,y1 = x,y
                o1 = compute_outcode(x1,y1,xmin,ymin, xmax,ymax)
            else:
                x2,y2 = x,y
                o2 = compute_outcode(x2,y2, xmin, ymin, xmax, ymax)
    return accepted, x1,y1,x2,y2

def visualize(window, line, title="Clipping"):
    fig, ax = plt.subplots(figsize=(10,5))
    xmin,ymin,xmax,ymax=window
    clip_rect = patches.Rectangle((xmin, ymin), xmax-xmin, ymax-ymin, linewidth=1.5, edgecolor='red', facecolor='none', linestyle='--')
    ax.add_patch(clip_rect)

    x1,y1,x2,y2 = line
    ax.plot([x1,x2],[y1,y2], 'gray', linestyle=':', marker='o', label='Original Line')

    accepted, clx1, cly1, clx2, cly2 = cohen_suth(x1,y1,x2,y2,xmin,ymin,xmax,ymax)

    if accepted:
        ax.plot([clx1,clx2],[cly1,cly2], 'blue', label='Clipped', marker='o')
        print(f"{title}: accepted")
    else:
        print(f"{title}: Rejected")
    ax.set_title(title)
    ax.set_xlim(0,20)
    ax.set_ylim(0,20)
    ax.set_aspect('equal', 'box')
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    CLIP_WINDOW = (5, 5, 15, 15)
    line_to_clip = (1, 1, 4, 4)
    line_title = "Single Crossing Line"
    visualize(CLIP_WINDOW, line_to_clip, line_title) 
