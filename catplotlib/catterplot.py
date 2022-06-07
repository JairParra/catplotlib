# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 12:59:01 2020
Last update: 2020-05-29

catterplot.py 
    This script contains the CatterPlot object, a wrapper for some Matplolib methods. 
    The main functionality is to produce easy, conventional plots using cats as backgrounds
    or points. 

@author: Hair Albeiro Parra Barrera
@website: https://jairparraml.com/ 
@linkedin: https://www.linkedin.com/in/hair-parra/
"""

##################################################################################
### 1. Imports ### 
##################################################################################

# general 
import os 
import pprint
import traceback
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
from typing import Union 
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# catplotliub 
import catplotlib
from catplotlib.utils import CatImg # contains paths to backgrounds and icons  

# global configurations 
pp = pprint.PrettyPrinter(indent=2)

##################################################################################
### 2. Class object ### 
##################################################################################

class CatterPlot():     
    """
    Catterplot wrapper object for Matplotlib methods. 
    

    Attributes
    ----------
    background: str
        specifies object instance background 
    figsize: tuple
        2-integer tuple specifying figsize argument used in matplolib
    transparency: int 
        Determines the dregee of transparency of the background image
        

    Methods
    -------
    """
    def __init__(self, 
                 background="nyan0", 
                 extent:str="auto", 
                 transparency=150, 
                 ): 
        """
        @args: 
            - background: Image background to use. 
                * "nyan0": Classic nyan cat
                * "nyan1": Nyan anime girl
            - extent: adjust x and y limits for actual figure 
                * 'auto': Obtains minimum and maximum of the data and 
                          graphs based on coordinates.  (DEPRECATE?)
        """
        self.background = background 
        self.extent = extent  # not used
        self.transparency = transparency 
        
        
    def _get_extent(self,x,y): 
        """
        Calculates background image extent limits given the input data.
        @args: 
            - X: list or array of numeric data. 
            - y: list or array of numeric data. 
        """ 
        return [min(x), max(x), min(y), max(y)] 
    
        
    def _load_meaowground(self, background=None, verbose:bool=True): 
        """
        Loads and returns chosen background. 
        @args: 
            - background: Integer representing background to choose. 
        """
        # throw an exception in case wrong background specified 
        if background not in CatImg.backgrounds.value.keys(): 
            error_msg = "Invalid background specified. Default background will be used." 
            error_msg += "\n\tCurrently supported abckgrounds are: "  
            error_msg += "CatImg.backgrounds.value.keys()"            
            raise ValueError(error_msg)
        
        try: 
            # use object background attribute if not specified
            if not background:
                if verbose: 
                    print(f"--Warning--: Using self.background={self.background}")
                meaowground = Image.open(CatImg.backgrounds.value[self.background])
            else: 
                # obtain full module base path
                basepath = os.sep.join(catplotlib.__file__.split("\\")[:-2])
                
                # obtain specific background
                catpath = CatImg.backgrounds.value[background]
                
                # join path to obtain specified imagepath 
                filename = basepath + os.sep + catpath   
                
                # ###############################
                # print("basepath: ", basepath) 
                # print("catpath: ", catpath) 
                # print("filename: ", filename)
                # ##############################
                                
                meaowground = Image.open(filename)
                                
        except Exception as e:    
            traceback.print_exc()
            
        return meaowground
    
    
    def _load_meawcon(self, icon:int=None): 
        """
        Loads icon that will be used instead of dots. 
        """ 
        
        # obtain full module base path
        basepath = os.sep.join(catplotlib.__file__.split("\\")[:-2])
        
        # obtain relative path to icon 
        if icon in list(range(0,14)): 
            pawth = CatImg.icons.value[f"icon{icon}"]
        else: 
            print("--Warning--: Invalid icon. Default will be loaded.")
            pawth = CatImg.icons.value["icon0"]
            
        # concatenate the path 
        meawcon = basepath + os.sep + pawth
            
        return meawcon
        
        
    def nyancatter(self, x, y, image:Union[str, np.array], ax=None, zoom:float=0.3):
        """
        Plots a Scatter plot of the input points. This function can be used in combination 
        with other functions to plot the cats instead of points, or it can be used on it's own. 
        
        @args: 
            -  x, y (float or array-like): x and y arguments compatible with matplotlib.pyplot.scatter. 
                                           paired together, will form the coordinates of the points to plot.
            - image (str | np.array): either a path to an image to load (if str), or a np.array of numbers
                                      representing an image. 
            - ax (??): 
            - zoom (float): determines the percentage of zoom of the points. Default is 0.3. 
                            A higher percentage will proportionally increase the zoom. Max is 1.0
        """
        # create axis if None
        if ax is None:
            ax = plt.gca()
            
        # control level of zoom 
        if zoom <= 0.0 or zoom > 3.0: 
            raise ValueError("Invalid zoom range. 'zoom' should have a value between 0.0 and 3.0")
            
        try:
            # use provided path to read an image
            image = plt.imread(image)
        except TypeError:
            # Likely already an array...
            pass
        
        # create offset 
        im = OffsetImage(image, zoom=zoom)
        x, y = np.atleast_1d(x, y)
        artists = []
        
        # annotate each of the points with the given image
        for x0, y0 in zip(x, y):
            ab = AnnotationBbox(im, (x0, y0), xycoords='data', frameon=False)
            artists.append(ax.add_artist(ab))
        ax.update_datalim(np.column_stack([x, y]))
        ax.autoscale()
        
        return artists
        
        
    def catterplot(self,
                   x,y, 
                   p:str='-o', 
                   cat:int=None, 
                   icon:int=None, 
                   extent:Union["str", list]="auto", 
                   figsize:tuple=(10,10), 
                   transparency:int=200, 
                   icon_zoom:float=0.3): 
        """
        Plots a sCATter plot 
        @args: 
            - x, y (float or array-like): x and y arguments compatible with matplotlib.pyplot.scatter. 
                                           paired together, will form the coordinates of the points to plot. 
            - p (str): kind of lines and points to plot. Patterns can be ['o', '-o', '--', ...] etc. 
            - cat (int): loads catground image. None by default will use default. 
            - icon (int): representing points to use. 
            - extent (str or list of 4): 
            - figsize (tuple of ints): figsize used in Matplotlib. 
            - transparency (int): The higher the value, the more transparency. Default is 200.
            - icon_zoom (float): 
            
        """
        # checks 
        if cat not in list(range(0,2)): 
            raise ValueError("Available backgrounds are 0, ..., 1 only. ")
        if icon not in list(range(0,14)): 
            raise ValueError("Available icons are only integers 0, 1, ..., 13.") 
        if transparency <= 0 or transparency > 300: 
            raise ValueError("'transparency' should be in the range (0, 300]")
        if len(x) != len(y): 
            raise ValueError("X and y must be one-dimensional arrays with the same lenght.") 
        if icon_zoom <= 0.0: 
            raise ValueError("icon_zoom must be positive")
        
        # obtain background to use
        meaowground = self._load_meaowground(background="nyan" + str(cat)) 
        meaowground.putalpha(transparency) # transparency  
        
        # Load icon path 
        icon_pawth = self._load_meawcon(icon)
        
        # Obtain image extent
        if isinstance(extent, str): 
            if extent == "auto": 
                extent = self._get_extent(x,y) 
            else: 
                raise ValueError("argument 'extent' must be 'auto' or a size 4 list [min_x, max_x, min_y, max_y]")
        
        # else if extent is a list of size 4 
        elif isinstance(extent, list) and len(extent) == 4: 
            # check that all elements are ints 
            if not all(list(map(lambda e: isinstance(e, int), extent))):
                raise ValueError("argument 'extent' must be 'auto' or a size 4 list [min_x, max_x, min_y, max_y]")

        # initialize plot 
        fig, ax = plt.subplots(figsize=figsize) 

        # Plot background  
        ax.imshow(meaowground, extent=extent)

        # Plot points if matching
        if p == "-o": 
            self.nyancatter(x,y, icon_pawth, ax=ax, zoom=icon_zoom)
        
        # display plot 
        plt.plot(x,y, p, color="white") 
        
        # Render
        plt.show() 
        
        
    def __print__(self): 
        """ 
        String representation of Catterplot object. 
        """
        s = f"CatterPlot(background={self.background})"
        return s
        