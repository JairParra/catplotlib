# -*- coding: utf-8 -*-
"""
### module_tests.py ### 

Created on Sun Oct  4 14:29:15 2020

@author: jairp
"""

#################################################################################

### 1. Imports ####  

import numpy as np 
import matplotlib.pyplot as plt 
from catplotlib.catplotlib.catterplot import CatterPlot


#################################################################################

### 2. Tests ####  


# load CatterPlot object 
cp = CatterPlot() 
 
# obtain background image (default)
bkg = cp.load_meaowground() 

# display image
fig, ax = plt.subplots()
ax.imshow(bkg, extent=[0, 400, 0, 300]) # change plotting dimensions 



