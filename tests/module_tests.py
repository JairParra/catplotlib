# -*- coding: utf-8 -*-
"""
### module_tests.py ### 

Created on Sun Oct  4 14:29:15 2020

@author: jairp
"""

#################################################################################

### 1. Imports ####  
from PIL import Image, ImageDraw, ImageFilter

from utils import CatImg
import numpy as np 
import matplotlib.pyplot as plt 
from catplotlib.catplotlib.catterplot import CatterPlot


#################################################################################

### 2. Tests ####  


# load CatterPlot object 
cp = CatterPlot() 
 
# obtain background image (default)
bkg = cp.load_meaowground(background=0)
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