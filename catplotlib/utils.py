# -*- coding: utf-8 -*-
"""
### utils.py ### 

Contains nyanutils for pussyntastic plots. 

Created on Sat Oct  3 13:04:52 2020

@author: jairp
"""

##################################################################################
### 1. Imports ### 
##################################################################################

import os 
import numpy as np
import matplotlib.pyplot as plt
from enum import Enum  # class to create enumeratiosn 
from PIL import Image, ImageDraw, ImageFilter 
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

os.path.realpath("__file__")

################################################################################## 
### 2. Enums ### 
##################################################################################

class CatImg(Enum): 
    """
    Contains information on background and symbol paths 9l.,..,
    """
    backgrounds = {"nyan0":"backgrounds\\nyan0.jpg",  
                   "nyan1":"backgrounds\\nyan1.jpg", 
                   }
    icons = {"icon0":"icons\\cat_icon0.png",
             "icon1":"icons\\cat_icon1.png",
             "icon2":"icons\\cat_icon2.png",
             "icon3":"icons\\cat_icon3.png",
             "icon4":"icons\\cat_icon4.png",
             "icon5":"icons\\cat_icon5.png",
             "icon6":"icons\\cat_icon6.png",
             "icon7":"icons\\cat_icon7.png",
             "icon8":"icons\\cat_icon8.png",
             "icon9":"icons\\cat_icon9.png",
             "icon10":"icons\\cat_icon10.png",
             "icon11":"icons\\cat_icon11.png",
             "icon12":"icons\\cat_icon12.png", 
             "icon13":"icons\\cat_icon13.png",
             }