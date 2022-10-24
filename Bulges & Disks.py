# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:47:30 2022

@author: devik
"""

import matplotlib.pyplot as plt

import seaborn as sns

# For classical bulges

# Reading data


x = [-22.62, -23.81, -24.69, -24.11, -22.93, -23.33, -20.99, -23.91, -23.41, -24.8, -23.24, -22.51, -21.55, -24.15, -22.65, -25.28, -20.82]
y = [8.155336037, 7.812913357, 8.938019097, 8.217483944, 7.615950052, 7.850033258, 7.161368002, 8.952792443, 8.378397901, 8.517195898, 8.926856709, 8.255272505, 7.5774918, 8.654176542, 7.944975908, 8.822821645, 6.954242509]

# Creating error

yerrormin = [1.12, 5.0, 8.21, 0.92, 3.71, 6.76, 0.31, 6.20, 1.63, 2.71, 7.79, 1.45, 3.74, 3.48, 6.38, 6.24, 0.36]

yerrormax = [2.34, 9.0, 9.61, 2.39, 4.56, 7.41, 1.65, 9.54, 2.66, 4.74, 9.15, 2.40, 3.82, 5.91, 11.26, 7.05, 1.43]

yerror = [yerrormin, yerrormax]



plt.figure(figsize = (10,8))
plt.xlabel('$M_{Ks,bulge}$')
plt.ylabel('log$M_{•}$($M_{⊙}$)')
plt.title('For Classical Bulges (In Spiral & S0 galaxies)')


# Plot scatter plot

plt.scatter(x,y)


# Plot error bar

#plt.errorbar(x,y,yerr=yerror, fmt = 'o')


#create scatterplot with regression line

sns.regplot(x, y, ci=None)


# For diks

# Reading data

x = [-23.85, -23.53, -22.04, -20.92, -23.41, -23.33, -22.18, -21.53, -22.49, -21.99, -21.36, -22.03, -23.71, -23.47, -21.88, -22.55, -22.02]

y = [8.155336037, 7.812913357, 8.938019097, 8.217483944, 7.615950052, 7.850033258, 7.161368002, 8.952792443, 8.378397901, 8.517195898, 8.926856709, 8.255272505, 7.5774918, 8.654176542, 7.944975908, 8.822821645, 6.954242509]

yerrormin = [1.12, 5.0, 8.21, 0.92, 3.71, 6.76, 0.31, 6.20, 1.63, 2.71, 7.79, 1.45, 3.74, 3.48, 6.38, 6.24, 0.36]

yerrormax = [2.34, 9.0, 9.61, 2.39, 4.56, 7.41, 1.65, 9.54, 2.66, 4.74, 9.15, 2.40, 3.82, 5.91, 11.26, 7.05, 1.43]

yerror = [yerrormin, yerrormax]


plt.figure(figsize = (10,8))
#plt.errorbar(x,y,yerr=yerror, fmt = 'o')
plt.xlabel('$M_{Ks,disk}$')
plt.ylabel('log$M_{•}$($M_{⊙}$)')
plt.title('For Disks (In Spiral & S0 galaxies)')

#create scatterplot with regression line

sns.regplot(x, y, ci=None)