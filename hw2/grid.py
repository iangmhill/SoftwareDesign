# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:38:37 2014

@author: ihill
"""

gridspacing = 4
columns = 4
rows = 4

def gridhor(spacing,col):
    print(("+ " + "- "*spacing)*col + "+")
def gridvert(spacing,col):
    print((("| " + "  "*spacing)*col + "| \n")*(spacing-1) + (("| " + "  "*spacing)*col + "| "))

for i in range(rows):
    gridhor(gridspacing,columns)
    gridvert(gridspacing,columns)
gridhor(gridspacing,columns)