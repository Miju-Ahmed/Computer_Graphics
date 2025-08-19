import numpy as np
import matplotlib.pyplot as plt

def plot_shape(shape, title="", color='blue'):
    plt.plot(shape[:, 0], shape[:, 1], color=color, marker='o', linestyle='-', label=title)
def get_translation_matrix(tx,ty):
    return np.array([
        [1,0,tx],
        [0,1,ty],
        [0,0,1]
    ])
def get_scaling_matrix(sx,sy):
    return np.array([
        [sx,0,0],
        [0,sy,0],
        [0,0,1]
    ])
def get_rotation_matrix(angle_degrees):
    angle_rad=np.radians(angle_degrees)
    cos_a=np.cos(angle_rad)
    sin_a=np.sin(angle_rad)
    return np.array([
        [cos_a,-sin_a,0],
        [sin_a,cos_a,0],
        [0,0,1]
    ])
def apply_transformation(shape,matrix):
    homogeneous_shape=np.hstack([shape,np.ones((shape.shape[0],1))])
    transformed_shape_homogeneous=(matrix@homogeneous_shape.T).T
    return transformed_shape_homogeneous[:,:2]
if __name__== "__main__":
    house_shape=np.array([
        [0, 0], [0, 10], [5, 15], [10, 10], [10, 0], [0, 0]
    ])
    tx,ty=20,5
    tranlation_matrix=get_translation_matrix(tx,ty)
    tranlated_house=apply_transformation(house_shape,tranlation_matrix)

    sx, sy = 1.5, 0.5
    scaling_matrix = get_scaling_matrix(sx, sy)
    scaled_house = apply_transformation(tranlated_house, scaling_matrix)

    angle = 45 
    rotation_matrix = get_rotation_matrix(angle)
    rotated_house = apply_transformation(scaled_house, rotation_matrix)

    plt.figure(figsize=(12, 10))
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    
    plot_shape(house_shape, "Original", 'gray')
    plot_shape(tranlated_house, f"Translated by ({tx}, {ty})", 'red')
    plot_shape(scaled_house, f"Scaled by ({sx}, {sy})", 'green')
    plot_shape(rotated_house, f"Rotated by {angle}°", 'purple')
    plt.title("2D Geometric Transformations")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()