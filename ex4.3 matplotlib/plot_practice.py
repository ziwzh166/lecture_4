# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:29:18 2022

@author: zhao
"""

import matplotlib.pyplot as plt
import numpy as np

#define three random functions
f1 = lambda x: -0.04*x**3+ 1*x**2 + 10
f2 = lambda x: 1.5*x**2+ 2*x**2 + 50
f3 = lambda x: 20000*np.sin(5*np.pi*x +5)

#define variables
x = np.linspace(1,100,num=50)
y1 = f1(x)
y2 = f2(x)
y3 = f3(x)
#plot
ax1 = plt.subplot(211)
ax1.plot(x,y1)
ax1.set_xlabel('x')
ax1.set_ylabel('y1')
# set.x
ax2 = plt.subplot(212)
ax2.plot(x,y2)
ax2.plot(x,y3)
ax2.set_xlabel('x')
ax2.set_ylabel('y2 and y3')
