import numpy as np
import matplotlib.pyplot as plt

def sgn(x):
    return np.sign(x)

def create_superellipsoid(a, b, c, e, n, u_res=100, v_res=100):
    u = np.linspace(-np.pi, np.pi, u_res)
    v = np.linspace(-np.pi / 2, np.pi / 2, v_res)
    
    u, v = np.meshgrid(u, v)

    x = a * (sgn(np.cos(v)) * np.abs(np.cos(v))**e) * (sgn(np.cos(u)) * np.abs(np.cos(u))**n)
    y = b * (sgn(np.cos(v)) * np.abs(np.cos(v))**e) * (sgn(np.sin(u)) * np.abs(np.sin(u))**n)
    z = c * (sgn(np.sin(v)) * np.abs(np.sin(v))**e)
    
    return x, y, z

def plot_3d_shape(x, y, z, title="Superellipsoid"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(x, y, z, cmap='plasma', edgecolor='none', alpha=0.9)
    
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    ax.set_title(title)
    
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    plt.show()

if __name__ == '__main__':
    radii_cube = (1, 1, 1)
    shape_params_cube = (0.2, 0.2) # (e, n)
    x_cube, y_cube, z_cube = create_superellipsoid(*radii_cube, *shape_params_cube)
    plot_3d_shape(x_cube, y_cube, z_cube, title="Superellipsoid: Rounded Cube (e=0.2, n=0.2)")

    radii_ellipsoid = (1.5, 1, 1) # a, b, c
    shape_params_ellipsoid = (1.0, 1.0) # (e, n)
    x_ell, y_ell, z_ell = create_superellipsoid(*radii_ellipsoid, *shape_params_ellipsoid)
    plot_3d_shape(x_ell, y_ell, z_ell, title="Superellipsoid: Ellipsoid (e=1.0, n=1.0)")
    
    radii_star = (1, 1, 1)
    shape_params_star = (2.0, 2.0) # (e, n)
    x_star, y_star, z_star = create_superellipsoid(*radii_star, *shape_params_star)
    plot_3d_shape(x_star, y_star, z_star, title="Superellipsoid: Star Shape (e=2.0, n=2.0)")

    radii_star = (3, 2, 2)
    shape_params_star = (3.0, 4.0) # (e, n)
    x_star, y_star, z_star = create_superellipsoid(*radii_star, *shape_params_star)
    plot_3d_shape(x_star, y_star, z_star, title="Superellipsoid: Random = (3.0, 4.0)")

    radii_star = (5, 5, 6)
    shape_params_star = (7.0, 7.0) # (e, n)
    x_star, y_star, z_star = create_superellipsoid(*radii_star, *shape_params_star)
    plot_3d_shape(x_star, y_star, z_star, title="Superellipsoid: Random = (7.0, 7.0)")