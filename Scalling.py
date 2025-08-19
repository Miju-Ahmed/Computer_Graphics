import numpy as np
import matplotlib.pyplot as plt

def plot_shape(shape, title="",color="blue"):
    plt.plot(shape[:,0],shape[:,1],color=color,marker='o',linestyle='-',label=title)

# def plot_shape(shape, title="", color='blue'):
    # plt.plot(shape[:, 0], shape[:, 1], color=color, marker='o', linestyle='-', label=title)


def get_scalling_matrix(sx,sy):
    return np.array([
        [sx,0,0],
        [0,sy,0],
        [0,0,1]
    ])
def apply_transformation(shape,matrix):
    homo_shape=np.hstack([shape,np.ones((shape.shape[0],1))])
    transformed_shape=(matrix@homo_shape.T).T
    return transformed_shape[:,:2]

if __name__== "__main__":
    house_shape=np.array([
        [0, 0], [0, 10], [5, 15], [10, 10], [10, 0], [0, 0]
    ])
    sx, sy = 1.5, 0.5
    scaling_matrix = get_scalling_matrix(sx, sy)
    scaled_house = apply_transformation(house_shape, scaling_matrix)

    plt.figure(figsize=(12, 10))
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    plot_shape(house_shape, "Original", 'gray')
    plot_shape(scaled_house, f"Scaled by ({sx}, {sy})", 'green')
    plt.title("2D Geometric Transformations")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()