# -*- coding: utf-8 -*-
""" cii using ml.
Data Source: India
"""
from os import system
from statsmodels.tsa.stattools import adfuller
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys # Python version
# Uncomment for debugging
#print('Python: {}'.format(sys.version))
import scipy # scipy
# Uncomment for debugging
#print('scipy: {}'.format(scipy.__version__))
import numpy # numpy
# Uncomment for debugging
#print('numpy: {}'.format(numpy.__version__))
import matplotlib # matplotlib
# Uncomment for debugging
#print('matplotlib: {}'.format(matplotlib.__version__))
import pandas # pandas
# Uncomment for debugging
#print('pandas: {}'.format(pandas.__version__))

import sklearn # scikit-learn
# Uncomment for debugging
#print('sklearn: {}'.format(sklearn.__version__))

import statsmodels # scikit-learn
# Uncomment for debugging
#print('statsmodels: {}'.format(statsmodels.__version__))

#%matplotlib inline

#clear terminal screen
system('clear')
# Initially checkup"repository": null,



#reading data CII dataset
state_sec = pd.read_csv("ciids.csv") #Importing data
print state_sec.head()
print state_sec.columns
#print '\n Data Types:'
#print state_sec.dtypes

#print ("*** Averadge value***")
#print (state_sec.mean())
#print ("*** Minimum value***")
#print (state_sec.min())
#print ("*** Maximum value***")
#print (state_sec.max())
#print ("*** Mode value***")
#print (state_sec.mode())
#print ("*** Rannge ***")


# what to plot... Kindly check the csv is location. As of now I am using my local file
data = np.genfromtxt('/home/alok/projects/cii/ciids.csv', delimiter=',', names=['x', 'y'])
# Initialize a Figure
fig = plt.figure()
plt.plot(state_sec['Year'],'g^', state_sec['CII'],'ro')

plt.title('Year wise Cost inflation Index')
plt.ylabel('Year')
plt.xlabel('Cost inflation Index')
plt.grid(False)
plt.show()
