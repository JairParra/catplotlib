# -*- coding: utf-8 -*-
"""
### utils.py ### 

Contains nyanutils for pussyntastic plots. 

Created on Sat Oct  3 13:04:52 2020

@author: jairp
"""

##################################################################################

### 1. Imports ### 

import numpy as np
import matplotlib.pyplot as plt
from enum import Enum  # class to create enumeratiosn 
from PIL import Image, ImageDraw, ImageFilter
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


################################################################################## 

### 2. Enums ### 

class CatImg(Enum): 
    """
    Contains information on background and symbol paths 
    """
    backgrounds = {"nyan0":"../backgrounds/nyan0.jpg"}
    icons = {"icon0":"../icons/cat_icon0.png"}

##################################################################################

### 2. Functions ### 

 