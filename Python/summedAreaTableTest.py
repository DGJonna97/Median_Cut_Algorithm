# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:29:35 2020

@author: KAFF
"""

import numpy as np

test = 'cheese.jpg'

def summed_area_table(img):
    
    table = np.zeros_like(img).astype(int)
    
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            
            if (row > 0) and (col > 0):
                table[row, col] = (img[row, col] +
                                   table[row, col - 1] +
                                   table[row -1, col] -
                                   table[row - 1, col - 1])
            
            elif row > 0:
                table[row, col] = img[row, col] + table[row -1, col]
                
            elif col > 0:
                table[row, col] = img[row, col] + table[row, col - 1]
                
            else:
                table[row, col] = img[row, col]
                
    return table

print(summed_area_table(test))

# Gives an int() with base 10: ' ' error