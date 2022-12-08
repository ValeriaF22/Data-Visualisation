# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:41:12 2022

@author: v.filippou
"""
#%%
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

#%%

def generate_random_data():
    # Random scatter 
    # Grid
    nx, ny = 50, 50
    x = range(nx)
    y = range(ny)   
    X, Y = np.meshgrid(x, y)

    # Multiple 2D arrays    
    nz = 50
    Z_list = []
    z = [Z_list.append(np.random.random((nz, nz))) for i in range(50)]
    
    return X, Y, Z_list

#%%

def generate_ackley_data():
    # Ackley function scatter
    # Grid
    x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    X,Y = np.meshgrid(x,y)
    
    # Multiple 2D arrays
    equation = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (X**2 + Y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * X) + np.cos(2 * np.pi * Y))) + np.e + 20
    nz = 100
    Z_list = []
    z = [Z_list.append(equation + np.random.random((nz, nz))) for i in range(50)]
    
    return X, Y, Z_list

#%%

# Create data using functions
X_rand, Y_rand, Z_list_rand = generate_random_data()

X_ackley, Y_ackley, Z_list_ackley = generate_ackley_data()

#%%
def create_animation(X, Y, Z_list):
    
    # Initial Z 2D array
    Z0 = Z_list[0]
    
    # Threshold values
    avg_Z = np.average(Z0)
    min_Z = np.min(Z0)
    max_Z = np.max(Z0)
    
    # Sequential selection of Z 2D arrays
    def some_data(i):   # function returns a 2D data array    
        return Z_list[i]
    
    # 3D plot
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
 
    # Initial graph
    graph = ax.scatter(X[Z0<avg_Z], Y[Z0<avg_Z], Z0[Z0<avg_Z], alpha=0.5, c='green') 
    graph = ax.scatter(X[Z0>avg_Z], Y[Z0>avg_Z], Z0[Z0>avg_Z], alpha=0.5, c='darkblue') 
    ax.set_zlim(min_Z, max_Z)
    
    # Animation function
    def animate(i):
        
        Z = some_data(i)
        
        # Plot
        ax.clear()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_zlim(min_Z, max_Z)
        graph = ax.scatter(X[Z<avg_Z], Y[Z<avg_Z], Z[Z<avg_Z], alpha=0.5, c='green') 
        graph = ax.scatter(X[Z>avg_Z], Y[Z>avg_Z], Z[Z>avg_Z], alpha=0.5, c='darkblue') 
        plt.title('Frame number: {}'.format(i))
        plt.show()
        
        return graph
    
    anim = animation.FuncAnimation(fig, animate, frames=50, repeat=True)
    # Save video as mp4
    # anim.save('ackley_scatter.mp4', writer=animation.FFMpegWriter())
    
    # Save gif
    # anim.save('ackley_scatter_gif.gif', fps=5)
    
    return anim
    
#%%
create_animation(X_rand, Y_rand, Z_list_rand)
#%%
create_animation(X_ackley, Y_ackley, Z_list_ackley)

