from math import *
import matplotlib.pyplot as plt
import random
import numpy as np
def print_circle(r):
    a = np.arange(-r,r,0.0001)
    b = np.sqrt(np.power(r,2)-np.power(a,2))
    plt.plot(a,b,color= 'r')
    plt.plot(a,-b,color= 'r')
def Check_Boundary(r,position):
    if(position[0]*position[0]+position[1]*position[1]<r*r):
        return True
    else:
        return False
def Addforce(velocity:list,dt:float):
    m = (4*pi*100*250*250*2.2e-24)/3.0 #kg
    F = random.random() #
    theta = random.random()*360
    delta_velocity = dt* F/m
    delta_x = delta_velocity*cos(theta*pi/180)
    delta_y = delta_velocity*sin(theta*pi/180)
    print(delta_x,delta_y)
    return [delta_x+velocity[0],delta_y+velocity[1]]

def Brownian_Motion(dt:float,timestep:int,diffusion:float, boundary:float,Start=[0,0]):
    traj =[Start]
    delta_r = sqrt(4*diffusion*dt)
    velocity = [0 , 0]
    for i in range(timestep):
        velocity = Addforce(velocity,dt)
        theta = random.random()*360
        delta_x = delta_r*cos(theta*pi/180)+velocity[0]*dt
        delta_y = delta_r*sin(theta*pi/180)+velocity[1]*dt
        new_position = [traj[-1][0]+delta_x,traj[-1][1]+delta_y]
        if not Check_Boundary(boundary,new_position):
            break
        else:
            print("Timestep: %d, Position: %f,%f"%(i,new_position[0],new_position[1]))
            traj.append(new_position)
            
    return traj
def plot_traj(traj):
    X = [_[0] for _ in traj]
    Y = [_[1] for _ in traj]
    plt.plot(X,Y)

N = 100
reach = 0
boundary = 1
timestep =1000
print_circle(boundary)
for i in range(2):

    traj1 = Brownian_Motion(0.001, timestep, 0.1, boundary)
    plot_traj(traj1)
    if len(traj1)<timestep:
        reach+=1
reach_rate = float(reach)/N
print("到达率：%f"%(reach_rate))
plt.show()


