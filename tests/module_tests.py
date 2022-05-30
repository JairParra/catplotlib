# -*- coding: utf-8 -*-
"""
### module_tests.py ### 

Created on Sun Oct  4 14:29:15 2020

@author: jairp
"""

#################################################################################

### 1. Imports ####  

#################################################################################

# modules for path and os managerment
import os 
import sys 

# # fint current and parent directory and append to FILEPATH
# currentdir = os.path.dirname(os.path.realpath('__file__'))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

# general modules 
import importlib 
import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image, ImageDraw, ImageFilter

# raw catplotlib modules 

# catplotlib modules 
from catplotlib import utils 
from catplotlib import catterplot 

# import catplotlib.utils as utils 
# import catplotlib.catterplot as catterplot 
from catplotlib.utils import CatImg
from catplotlib.catterplot import CatterPlot 

# reload modules quickly  
# importlib.reload(utils)

#################################################################################

### 2. Tests ####  


# load CatterPlot object 
cp = CatterPlot() 
 
# obtain background image (default)
bkg = cp.load_meaowground(background="nyan1")

bkg.putalpha(150)

# display image
fig, ax = plt.subplots()
ax.imshow(bkg, extent=[0, 400, 0, 300]) # change plotting dimensions 


## Testing catterplot function 

X = [50,100,150,200,250,300,350] 
y = [30,10,56,100,250,200,300] 

cp = CatterPlot() 
cp.catterplot(X, y, p='-o', cat=1, icon=0, zoom = 0.3)

cp.load_meaowground(background="nyan" + str(1)) 

