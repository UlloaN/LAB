#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import sys

x=np.array([0.4,0.5,0.6,0.7,0.8,1.05])
#A=1404.0
#B=1725.40
#C=1663.14
#k=(4*(3.14)**2)/9.8 
#y1=np.sqrt(k*(((A*(x**2))+B)/((A*x)+C)))
#plt.plot(x,y1,'r-')

y=np.array ([1.67,1.7,1.74,1.79,1.86,2.04])

def func(x,h,a,b,c):                                       	
	    return np.sqrt(h*(((a*(x**2))+b)/((a*x)+c)))

param, otracosa=curve_fit(func,x,y)
print param

plt.plot(x,y,'r.')
plt.plot(x,func(x,*param),'b-')

#savefig...

plt.show()
