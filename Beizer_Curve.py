import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def beizer_curve(control_points,n_points=100):
    n=len(control_points)-1
    if(n<1):
        raise ValueError("At least two points are required.")
    control_points=np.array(control_points,dtype=float)
    t=np.linspace(0,1,n_points)
    curve=np.zeros((n_points,2))
    for i in range(n+1):
        bernstein_ply=comb(n,i)*(t**i)*((1-t)**(n-i))
        curve+=np.outer(bernstein_ply,control_points[i])
    return curve
def plot_curve_with_control_points(curve,control_points,title="Beizer Curve"):
    control_points=np.array(control_points)
    plt.figure(figsize=(10,8))
    plt.plot(curve[:,0],curve[:,1],"b-",lw=2,label="Beizer Curve")
    plt.plot(control_points[:,0],control_points[:,1],'ro--',label='Control Polygon')
    plt.plot(control_points[:,0],control_points[:,1],'go',markersize=10,label="Control Points")
    for i, (x,y) in enumerate(control_points):
        plt.text(x+5,y,f'P{i}',fontsize=14,verticalalignment='bottom')
    plt.title(title,fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__=="__main__":
    quadratic_control_points = [
        (50, 250),   # P0
        (150, 50),   # P1
        (250, 250),   # P2
        (350, 350),   # P0
        (0, 650),   # P1
        (550, 750)
    ]
    quadratic_curve = beizer_curve(quadratic_control_points)
    plot_curve_with_control_points(quadratic_curve, quadratic_control_points, 
                             title="Quadratic Bézier Curve")