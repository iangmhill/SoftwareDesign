# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:34:57 2014

@author: pruvolo
"""

# you do not have to use these particular modules, but they may help
from random import randint
from math import pi, sqrt, sin, cos
import Image

def build_random_function(min_depth, max_depth):
    """ build_random_function uses random numbers to construct a random function using recursion.
        INPUTS : minimum depth of function nesting, maximum depth of function nesting
        OUTPUT : a random function in the form of a lists of strings nested inside lists of strings
    """
    if min_depth <= 1 and max_depth > 1:
        q = randint(1,7)
        if q == 1:
            return ["prod",build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        elif q == 2:
            return ["cos_pi",build_random_function(min_depth-1, max_depth-1)]
        elif q == 3:
            return ["sin_pi",build_random_function(min_depth-1, max_depth-1)]
        elif q == 4:
            return ["x"]
        elif q == 5:
            return ["y"]
        elif q == 6:
            return ["avg",build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        elif q == 7:
            return ["sqrt",build_random_function(min_depth-1, max_depth-1)]
    elif max_depth <= 1:
        q = randint(1,2)
        if q == 1:
            return ["x"]
        elif q == 2:
            return ["y"]
    else:
        q = randint(1,5)
        if q == 1:
            return ["prod",build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        elif q == 2:
            return ["cos_pi",build_random_function(min_depth-1, max_depth-1)]
        elif q == 3:
            return ["sin_pi",build_random_function(min_depth-1, max_depth-1)]
        elif q == 4:
            return ["avg",build_random_function(min_depth-1, max_depth-1),build_random_function(min_depth-1, max_depth-1)]
        elif q == 5:
            return ["sqrt",build_random_function(min_depth-1, max_depth-1)]


def evaluate_random_function(f, x, y):
    """ Taks a nested lists of strings built to be a function and evaulates that function
        using x and y as inputs
        INPUTS: list of strings representing a function
        x value at which to evaluate the function, y value at which to evaluate the function
        OUTPUTS: a scalar value resulting from the function being evaulated
    """

    if f[0] == "prod":
        return float(evaluate_random_function(f[1], x, y))*float(evaluate_random_function(f[2], x, y))
    elif f[0] == "cos_pi":
        return cos(pi*float(evaluate_random_function(f[1], x, y)))
    elif f[0] == "sin_pi":
        return sin(pi*float(evaluate_random_function(f[1], x, y)))
    elif f[0] == "avg":
        return (float(evaluate_random_function(f[1], x, y))+float(evaluate_random_function(f[2], x, y)))/2.0
    elif f[0] == "sqrt":
        return sqrt(abs(float(evaluate_random_function(f[1], x, y))))
    elif f[0] == "x":
        return x
    elif f[0] == "y":
        return y
    

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Maps the input value that is in the interval [input_interval_start, input_interval_end]
        to the output interval [output_interval_start, output_interval_end].  The mapping
        is an affine one (i.e. output = input*c + b).
        
        This function defines a scale factor by divding the magitude of the output interval by that of the input interval.
        The value is multiplied by the scale factor and shifted into the output interval.
    """
    scale_factor = ((output_interval_end-output_interval_start)/(input_interval_end-input_interval_start))
    #print scale_factor
    return val*scale_factor + (output_interval_start-input_interval_start*scale_factor)

red = build_random_function(12,15)
green = build_random_function(2,5)
blue = build_random_function(8,10)

image_size = [1000,1000]

im = Image.new("RGB",image_size)
pixels = im.load()
for i in range(im.size[0]):
    message = "Generating image: " + str(int((float(i)/image_size[0])*100)) + "% complete"
    print(message)
    for j in range(im.size[1]):
        x = remap_interval(i,0.0,float(image_size[0]),-1.0,1.0)
        y = remap_interval(j,0.0,float(image_size[1]),-1.0,1.0)
        #print [x,y]
        r = int(remap_interval(evaluate_random_function(red,x,y),-1.0,1.0,0.0,255.0)*.7)
        g = int(remap_interval(evaluate_random_function(green,x,y),-1.0,1.0,0.0,255.0))
        b = int(remap_interval(evaluate_random_function(blue,x,y),-1.0,1.0,0.0,255.0))
        #print [r,g,b]
        pixels[i,j] = (r,g,b)
print pixels
im.save("image11.png")