from math import *
import matplotlib.pyplot as plt
import random


def Check_Boundary(r,position):
    if(position[0]*position[0]+position[1]*position[1]<r*r):
        return True
    else:
        return False

def Brownian_Motion(dt:float,timestep:int,diffusion:float, boundary:float,Start=[0,0]):
    traj =[Start]
    delta_r = sqrt(4*diffusion*dt)
    for i in range(timestep):
        theta = random.random*360
        delta_x = delta_r*cos(theta*pi/360)
        delta_y = delta_r*sin(theta*pi/360)
        new_position = [traj[-1][0]+delta_x,traj[-1][1]+delta_y]
        if not Check_Boundary(boundary,new_position):
            break
        else:
            traj.append(new_position)
    return traj
def plot_traj(traj):
    X = [_[0] for _ in traj]
    Y = [_[1] for _ in traj]
    plt.plot(X,Y)
traj1 = Brownian_Motion(0.001, 1000, 0.1, 1)
plot_traj(traj1)
plt.show()
