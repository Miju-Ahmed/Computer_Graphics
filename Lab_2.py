import matplotlib.pyplot as plt
import matplotlib.patches as patches

INSIDE=0
LEFT=1
RIGHT=2
BOTTOM=4
UP=8

def compute_outcode(x,y,xmin,ymin,xmax,ymax):
    code=INSIDE
    if x<xmin:
        code|=LEFT
    elif x>xmax:
        code|=RIGHT
    if y<ymin:
        code|=BOTTOM
    elif y>ymax:
        code|=UP
    return code

def cohen_sutherland_clip(x1,y1,x2,y2,xmin,ymin,xmax,ymax):
    outcode1=compute_outcode(x1,y1,xmin,ymin,xmax,ymax)
    outcode2=compute_outcode(x2,y2,xmin,ymin,xmax,ymax)
    accepted=False

    while True:
        if not(outcode1|outcode2):
            accepted=True
            break
        elif (outcode1&outcode2):
            break
        else:
            outcode_out=outcode1 if outcode1 else outcode2
            x,y=0,0
            
            if outcode_out&UP:
                x=x1+(x2-x1)*(ymax-y1)/(y2-y1)
                y=ymax
            elif outcode_out&BOTTOM:
                x=x1+(x2-x1)*(ymin-y1)/(y2-y1)
                y=ymin
            elif outcode_out&LEFT:
                y=y1+(y2-y1)*(xmin-x1)/(x2-x1)
                x=xmin
            elif outcode_out&RIGHT:
                y=y1+(y2-y1)*(xmax-x1)/(x2-x1)
                x=xmax
            
            if outcode_out==outcode1:
                x1,y1=x,y
                outcode1=compute_outcode(x1,y1,xmin,ymin,xmax,ymax)
            else:
                x2,y2=x,y
                outcode2=compute_outcode(x2,y2,xmin,ymin,xmax,ymax)
    return accepted,x1,y1,x2,y2
    
def visualize_clipping(window,lines):
    fig, ax = plt.subplots(1, len(lines), figsize=(5 * len(lines), 5))
    if len(lines) == 1:
        ax = [ax] 

    xmin, ymin, xmax, ymax = window

    for i, (title, line) in enumerate(lines.items()):
        x1, y1, x2, y2 = line
        
        clip_rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, 
                                      linewidth=1.5, edgecolor='red', facecolor='none', linestyle='--')
        ax[i].add_patch(clip_rect)
        
        ax[i].plot([x1, x2], [y1, y2], 'gray', linestyle=':', marker='o', label='Original Line')
        
        accepted, cl_x1, cl_y1, cl_x2, cl_y2 = cohen_sutherland_clip(x1, y1, x2, y2, xmin, ymin, xmax, ymax)
        
        if accepted:
            ax[i].plot([cl_x1, cl_x2], [cl_y1, cl_y2], 'blue', marker='o', label='Clipped Line')
            print(f"'{title}': Accepted. Clipped to ({cl_x1:.2f}, {cl_y1:.2f}) - ({cl_x2:.2f}, {cl_y2:.2f})")
        else:
            print(f"'{title}': Rejected.")

        ax[i].set_title(title)
        ax[i].set_xlim(0, 20)
        ax[i].set_ylim(0, 20)
        ax[i].set_aspect('equal', adjustable='box')
        ax[i].legend()
        ax[i].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Define the clipping window
    CLIP_WINDOW = (5, 5, 15, 15)  # (xmin, ymin, xmax, ymax)

    # Define various line segments to test the algorithm
    test_lines = {
        "1. Fully Inside": (6, 6, 14, 14),
        "2. Fully Outside (Reject)": (1, 1, 4, 4),
        "3. Crossing One Boundary": (1, 10, 10, 10),
        "4. Crossing Two Boundaries": (4, 18, 16, 2),
        "5. Diagonal Corner Crossing": (16, 16, 4, 4),
        "6. Vertical Line": (10, 1, 10, 19),
    }

    visualize_clipping(CLIP_WINDOW, test_lines)