from math import *
import matplotlib.pyplot as plt
import random
import numpy as np
def velocity_r(r:float,u:float,R:float):
    if(r>R):
        return 0
    else:
        return 2*u*(1-r*r/(R*R))
def print_circle(r):
    a = np.arange(-r,r,r*0.0001)
    b = np.sqrt(np.power(r,2)-np.power(a,2))
    plt.plot(a,b,color= 'r')
    plt.plot(a,-b,color= 'r')
def Check_Boundary(r,position):
    if(position[0]*position[0]+position[1]*position[1]<r*r):
        return True
    else:
        return False
def F_alpha(v_average):
    #lpha:0-180
    # al = [0,11.7,20.7,23.6,20.7,12.1,0,-12.1,-20.7,-23.6,-20.7,-11.7,0]
    mean = 0.0449
    # id = int(alpha/15)
    # # low = al[id]
    # if(id ==12):
    #     return random.gau
    # else:
    return mean*v_average*1.03e-10


def Addforce(v_average:float,dt:float,alpha:float,alpha2:float,Dr:float,Dr2:float):
    new_alpha = random.gauss(alpha,sqrt(4*Dr*dt)*180/pi)%180
    new_alpha2 = random.random()*360
    m = (4*pi*100*250*250*2.2e-24)/3.0 #kg
    
    F = F_alpha(v_average) #
    delta_dis = dt*dt* F/m *0.5
    delta_x = delta_dis*cos(new_alpha2*pi/180)
    delta_y = delta_dis*sin(new_alpha2*pi/180)
    #print(delta_x,delta_y,velocity)
    return [[delta_x,delta_y],new_alpha,alpha2]

def Brownian_Motion(dt:float,timestep:int,diffusion:float,u:float,m:float, boundary:float,Dr:float,Dr2:float,Start=[0,0]):
    kB = 1.38e-23
    alpha = random.random()*180
    alpha2 = random.random()*360
    traj =[Start]
    delta_r = sqrt(4*diffusion*dt)
    for i in range(timestep):
        theta = random.random()*360
        new_x = delta_r*cos(theta*pi/180) +traj[-1][0]
        new_y = delta_r*sin(theta*pi/180) +traj[-1][1]
        r_new = sqrt(pow(new_x,2)+ pow(new_y,2))
        r_origin = sqrt(pow(traj[-1][0],2)+pow(traj[-1][1],2))
        v_new = velocity_r(r_new,u,boundary)
        v_origin = velocity_r(r_origin,u,boundary)
        #计算平均速度
        v_average = m*abs(v_new-v_origin)*diffusion/(kB*310*dt)


        dis,alpha,alpha2 = Addforce(v_average,dt,alpha,alpha2,Dr,Dr2)
        dis =[0,0]
        delta_x = delta_r*cos(theta*pi/180)+dis[0]
        delta_y = delta_r*sin(theta*pi/180)+dis[1]
        new_position = [traj[-1][0]+delta_x,traj[-1][1]+delta_y]
        time = i*dt
        if not Check_Boundary(boundary,new_position):
            break
        else:
            if(i%100==0):
                print("Time: %f, Position: %f,%f"%(time,new_position[0],new_position[1]))
            traj.append(new_position)
            
    return traj
def plot_traj(traj):
    X = [_[0] for _ in traj]
    Y = [_[1] for _ in traj]
    plt.plot(X,Y)

N = 1000
reach = 0
boundary = 0.002
timestep =150000
diffusion = 1.895e-11
u = 0.18
m = (4*pi*100*250*250*2.2e-24)/3.0
Dr = 215.9
record_data = []
Dr2 = 215.9
print_circle(boundary)


for i in range(N):
#dt:float,timestep:int,diffusion:float,u:float,m:float, boundary:float,Dr:float,Dr2:float,Start=[0,0]
    traj1 = Brownian_Motion(1, timestep, diffusion, u, m, boundary,Dr,Dr2)
    plot_traj(traj1)
    record_data.append(str(len(traj1))+'\n')
    if len(traj1)<timestep:
        reach+=1
with open('C:/Users/tony1/Documents/ellip/ellipisoid_no_consider_force.txt','w') as f:
        f.writelines(record_data)    
reach_rate = float(reach)/N
print("到达率：%f"%(reach_rate))
plt.show()


