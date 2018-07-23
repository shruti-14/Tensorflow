# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 14:30:28 2018

@author: 212613023
"""

import numpy as np
import tensorflow as tf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize']= (10,6)
X= np.arange(0.0,5.0,0.1)

a=2
b=0

Y=a*X+b

plt.plot(X,Y)
plt.ylabel('Dependent Variable')
plt.xlabel('Independen Vaeiable')
plt.show()

