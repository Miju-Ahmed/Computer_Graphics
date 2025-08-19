import numpy as np
import matplotlib.pyplot as plt

def create_torus(R, r, u_res=50, v_res=30):
    u = np.linspace(0, 2*np.pi, u_res)
    v = np.linspace(0, 2*np.pi, v_res)

    u,v = np.meshgrid(u,v)

    # #Torus
    x = (R+r*np.cos(v))*np.cos(u)
    y = (R+r*np.cos(v))*np.sin(u)
    z = r*np.sin(v)

    return x, y, z
def plot_torus(x,y,z):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,z,cmap='viridis',edgecolor='none',alpha=0.8)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title('Torus Shape')

    ax.set_box_aspect([np.ptp(x), np.ptp(y), np.ptp(z)])

    plt.show()

if __name__ == '__main__':
    major_radius = 10  
    minor_radius = 5 

    torus_x, torus_y, torus_z = create_torus(major_radius, minor_radius)
    
    plot_torus(torus_x, torus_y, torus_z)