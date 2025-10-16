import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

def Beizer_curve(control_points, n_points=100):
    n = len(control_points)-1
    if n<1:
        raise ValueError("At least two points required")
    control_points = np.array(control_points, dtype=float)
    t = np.linspace(0,1,n_points)
    curve = np.zeros((n_points, 2))
    for i in range(n+1):
        bernstain_polygon = comb(n,i)*(t**i)*((1-t)**(n-i))
        curve += np.outer(bernstain_polygon, control_points[i])
    return curve
def plot_curve_with_control_points(curve,control_points, title='Beizer Curve'):
    control_points = np.array(control_points)
    plt.figure(figsize=(10,8))
    plt.plot(curve[:,0],curve[:,1], 'b-', lw=2, label='Beizer Curve')
    plt.plot(control_points[:,0],control_points[:,1],'ro--',label='Control Points')
    for i, (x,y) in enumerate(control_points):
        plt.text(x+5,y,f'P{i}', fontsize=15,  verticalalignment ='bottom')
    plt.title(title,fontsize=16)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

if __name__=="__main__":
    cp=[(50,250),(150,-250),(200,250),(250,-250),(300,200),(150,250),(200,180)]
    curve=Beizer_curve(cp)
    plot_curve_with_control_points(curve,cp,title="Quadric Beizer Curve")