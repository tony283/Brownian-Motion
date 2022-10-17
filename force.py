import random
import numpy as np
from math import *
def mean_list(l):
    add=0
    for i in range(len(l)):
        add+=l[i]
    return add/len(l)
def std_list(l):
    mean = mean_list(l)
    a = [pow((_-mean),2) for _ in l]
    return sqrt(mean_list(a))
def F_m(F):
    return sqrt(F[0]*F[0]+F[1]*F[1])
def F_alpha(alpha:float):
    #lpha:0-180
    al = [0,11.7,20.7,23.6,20.7,12.1,0,-12.1,-20.7,-23.6,-20.7,-11.7,0]
    id = int(alpha/15)
    low = al[id]
    if(id ==12):
        return random.gau
    else:
        return (low + (al[id+1]-low)*(alpha/15-id))

alpha = random.random()*180
alpha2 = random.random()*360

Flist =[0]
for j in range(100):
    print(j)
    F0 =[0,0]
    for i in range(100000):
        
        alpha = random.gauss(alpha,0.09*180/pi)%180
        alpha2 = random.gauss(alpha2,0.09*180/pi)%360
        F = F_alpha(alpha)/100000
        F0[0]+=F*cos(alpha2)
        F0[1]+=F*sin(alpha2)
    Flist.append(F_m(F0))
    
print(Flist)

print(mean_list(Flist))
print(std_list(Flist))


