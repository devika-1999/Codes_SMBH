# -*- coding: utf-8 -*-
"""
Created on Wed May 11 15:38:48 2022

@author: lenovo
"""

import numpy as np
from scipy import optimize 
import matplotlib.pyplot as plt
import csv

# For classical bulges

# Reading data

with open("Tab1.csv", "r") as i:
    Graph1 = list(csv.reader(i, delimiter = ","))
    
Tab1 = np.array(Graph1[1:], dtype = float)
x = Tab1[:,0]
y = Tab1[:,1]
yerror = 0.09

def func(x, a, b):
    y = a*x + b
    return y

alpha = optimize.curve_fit(func, xdata = x, ydata = y)[0]
print(alpha)

# plot the results

plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.errorbar(x, y, yerr=yerror, fmt='o')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('$M_{Ks,bulge}$')
plt.ylabel('log$M_{•}$/$M_{⊙}$')
plt.title('For Classical Bulges (In Spiral & S0 galaxies)')
plt.show()

# For disk of spiral S0 galaxies

with open("Tab2.csv", "r") as i:
    Graph2 = list(csv.reader(i, delimiter = ","))
    
Tab2 = np.array(Graph2[1:], dtype = float)
x = Tab2[:,0]
y = Tab2[:,1]
yerror = 0.09

def func(x, a, b):
    y = a*x + b
    return y

alpha = optimize.curve_fit(func, xdata = x, ydata = y)[0]
print(alpha)

# plot the results

plt.figure(figsize = (10,8))
plt.plot(x, y, 'b.')
plt.errorbar(x, y, yerr=yerror, fmt='o')
plt.plot(x, alpha[0]*x + alpha[1], 'r')
plt.xlabel('$M_{Ks,disk}$')
plt.ylabel('log$M_{•}$/$M_{⊙}$')
plt.title('For Disks (In Spiral & S0 galaxies)')
plt.show()



