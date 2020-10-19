# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:59:01 2020

@author: jairp
"""

##################################################################################

### 1. Imports ### 

import utils 
import pprint
import numpy as np
import matplotlib.pyplot as plt
from utils import CatImg # contains paths to backgrounds and icons 
from PIL import Image, ImageDraw, ImageFilter
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# global configurations 
pp = pprint.PrettyPrinter(indent=2)

##################################################################################

### 2. Class object ### 

class CatterPlot(): 
    """
    Catterplot wrapper object for Matplotlib methods. 
    """
    def __init__(self, 
                 background="nyan0", 
                 figsize=(10,10),  
                 extent="auto", 
                 transparency=150, 
                 ): 
        """
        @args: 
            - background: Image background to use. 
                * "nyan0": Classic nyan cat
            - figsize: adjust matplotlib figure size whenever proper 
            - extent_type: adjust x and y limits for actual figure 
                * 'auto': Obtains minimum and maximum of the data and 
                          graphs based on coordinates. 
        """
        self.background = background 
        self.figsize = figsize  
        self.extent = extent 
        self.transparency = transparency 
        
        
    def get_extent(self,X,y): 
        """
        Calculates background image extent limits given the input data.
        @args: 
            - X: list or array of numeric data. 
            - y: list or array of numeric data. 
        """ 
        return [min(X), max(X), min(y), max(y)] 
    
        
    def load_meaowground(self, background=None): 
        """
        Loads and returns chosen background. 
        @args: 
            - background: Integer representing background to choose. 
        """
        
        try: 
            if not background: 
                meaowground = Image.open(CatImg.backgrounds.value[self.background])
            else: 
                meaowground = Image.open(CatImg.backgrounds.value[background])
        except Exception as e: 
            print("--WARNING--: Invalid background specified. Default background will be used.") 
            print("\tCurrently supported abckgrounds are: ") 
            pp.pprint(CatImg.backgrounds.value.keys())
            meaowground = Image.open(CatImg.backgrounds.value[self.background])
            
        return meaowground
    
    
    def load_meawcon(self, icon=None): 
        """
        Loads icon that will be used instead of dots. 
        """ 
        if isinstance(icon, int) and icon >= 0: 
            pawth = CatImg.icons.value["icon{}".format(icon)]
        else: 
            pawth = CatImg.icons.value["icon0"]
            
        return pawth 
        
        
    def nyancatter(self, X, y, image, ax=None, zoom=1):
        """
        Plots a Scatter plot of the input points. This function can be used in combination 
        with other functions to plot the cats instead of points, or it can be used on it's own. 
        """
        if ax is None:
            ax = plt.gca()
        try:
            image = plt.imread(image)
        except TypeError:
            # Likely already an array...
            pass
        im = OffsetImage(image, zoom=zoom)
        X, y = np.atleast_1d(X, y)
        artists = []
        for x0, y0 in zip(X, y):
            ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
            artists.append(ax.add_artist(ab))
        ax.update_datalim(np.column_stack([X, y]))
        ax.autoscale()
        return artists
        
        
    def catterplot(self,X,y,p='-o',cat=None, icon=None, figsize=(10,10), zoom=0.3): 
        """
        Plots a sCATter plot 
        @args: 
            - p: kind of lines to plot 
            - cat: int --> loads catground image. None by default will use default. 
            - icon: int representing points to use. 
        """
        if len(X) != len(y): 
            raise ValueError("X and y must be one-dimensional arrays with the same lenght.") 
        
        # TODO: Complete this function 
        meaowground = self.load_meaowground(background="nyan" + str(cat)) 
        meaowground.putalpha(150) # transparency  
        
        # Load icon path 
        icon_pawth = self.load_meawcon(icon)
        
        # Obtain image extent
        extent = self.get_extent(X,y) 

        # initialize plot 
        fig, ax = plt.subplots(figsize=figsize) 

        # Plot background  
        ax.imshow(meaowground, extent=extent)

        # Plot actual
        if p == "-o": 
            self.nyancatter(X,y, icon_pawth, ax=ax, zoom=zoom)
        
        # display plot 
        plt.plot(X,y, p, color="white") 
        
        # Render
        plt.show() 
        
        