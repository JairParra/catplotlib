# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:13:03 2020

@author: jairp
"""

###############################################################################
### 1. Imports ### 
import setuptools 

##############################################################################
### 2. Setting up ### 

with open("README.md", "r") as fh:
    long_description = None

setuptools.setup(
    name="catplotlib", # Replace with your own username
    version="1.0.0", 
    author="Hair Parra",
    author_email="jair.parra@outlook.com",
    description="Matplotlib. But with cats. ฅ(＾・ω・＾ฅ)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject", ## TODO: Update with proj repository 
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)