import matplotlib.pyplot as plt
import numpy as np

def plot_shape(shape, title="", color="blue"):
    plt.plot(shape[:,0],shape[:,1],color=color, marker='o', linestyle='-', label=title)
def get_scaling_matrix(sx,sy):
    return np.array([
        [sx,0,0],
        [0,sy,0],
        [0,0,1]
    ])
def get_translation(tx,ty):
    return np.array([
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ])

def get_rotation_matrix(angles):
    cos_a = np.cos(angles)
    sin_a = np.sin(angles)

    return np.array([
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0,0,1]
    ])

def transformation(shape, matrix):
    homogeneous_shape = np.hstack([shape,np.ones((shape.shape[0],1))])
    transformed_shape = (matrix@homogeneous_shape.T).T
    return transformed_shape[:,:2]
