import numpy as np
from numpy import linspace
import matplotlib.pyplot as plt
import math
import random





listpointsa = []

listpointsb = []


listpointscolors = []
listpointsfaileda = []
listpointsfailedb = []




def check1(a,b):
    i = complex(a,b)
    z0 = 0
    counter = 0
          
    while counter < 41:
            
        
        
        y = z0*z0 + i
        z0 = y
        counter += 1
        if counter > 40:
            break
        if counter == 40:
            
            
            if (y.real*y.real + y.imag*y.imag - 2*y.real*y.imag) <= 100:
                listpointsa.append(i.real)
                listpointsb.append(i.imag)
                
                
                listpointsfaileda.append(y.real*y.real + y.imag*y.imag)
            else:
                break
            
                    
        else: 
            pass

lista = []
listb = []
def check2():
    set1 = np.linspace(-2,1,1000)
    set2 = np.linspace(-1,1,1000)
    counter2 = 0
    u = 0
    t = 0
    while counter2 < 1001:
        a = u
        a = set1[a]
        b = t
        b = set2[b]
        check1(a,b)
        counter2 += 1
        u += 1
        if counter2 == 1000:
            counter2 = 0
            u = 0
            t += 1
            if t == 1000:
                break
            else: 
                pass
        
    
    
        
check2()

constant = 1/(max(listpointsfaileda))

for value in listpointsfaileda:
    listpointscolors.append([0,0,value*constant])




a = plt.axes()
a.set_facecolor([0,0,1])
a.set_aspect('equal')
plt.xlabel('real')
plt.ylabel('imag')
plt.title('Mandelbrot set')
plt.scatter(listpointsa,listpointsb,c=listpointscolors,linewidth = 1,s = 0.001)


plt.show()