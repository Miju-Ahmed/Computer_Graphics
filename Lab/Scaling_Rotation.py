import matplotlib.pyplot as plt
import numpy as np

def plot_shape(shape, title="", color='blue'):
    plt.plot(shape[:, 0], shape[:, 1], color=color, marker='o', linestyle='-', label=title)


def get_scaling_matrix(sx,sy):
    return np.array([
        [sx,0,0],
        [0,sy,0],
        [0,0,1]
    ])
def get_rotation_matrix(angles):
    cos_a=np.cos(angles)
    sin_a=np.sin(angles)
    return np.array([
        [cos_a,-sin_a,0],
        [sin_a,cos_a,0],
        [0,0,1]
    ])


def transformation(shape,matrix):
    homogeneous_shape=np.hstack([shape,np.ones((shape.shape[0],1))])
    transformed_shape=(matrix@homogeneous_shape.T).T
    return transformed_shape[:,:2]

if __name__=="__main__":
    house_shape=np.array([
        [0, 0], [0, 10], [5, 15], [10, 10], [10, 0], [0, 0]
    ])
    
    sx,sy=2,0.5
    scaling_matrix= get_scaling_matrix(sx,sy)
    scaled_house= transformation(house_shape,scaling_matrix)
    angles=75
    rotation_matrix= get_rotation_matrix(angles)
    scaled_rot_house= transformation(scaled_house,rotation_matrix)

    plt.figure(figsize=(12,8))
    ax=plt.gca()
    ax.set_aspect('equal',adjustable='box')
    plot_shape(house_shape,"Original",'gray')
    plot_shape(scaled_rot_house,f"Scaled and Rotated","purple")
    plt.title("2D Geometric Transformations")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()