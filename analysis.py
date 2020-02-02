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



#reading data Right Now Tamilnadu Petro only
state_sec = pd.read_csv("ciids.csv")
print state_sec.head()
#print '\n Data Types:'
#print state_sec.dtypes

print ("*** Averadge value***")
print (state_sec.mean())
print ("*** Minimum value***")
print (state_sec.min())
print ("*** Maximum value***")
print (state_sec.max())
print ("*** Mode value***")
print (state_sec.mode())
print ("*** Rannge ***")
