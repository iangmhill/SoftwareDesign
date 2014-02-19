# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:15:11 2014

@author: ihill
"""
from random import random

def get_complementary_base(base1):
    if type(base1) != str:
        return 'Please input a string.'
    elif base1 == 'T':
        return 'A'
    elif base1 == 'A':
        return 'T'    
    elif base1 == 'G':
        return 'C'
    elif base1 == 'C':
        return 'G'
    else:
        return 'This is not a nucleotide.'
        
def is_between(x,y,z):
    if x < y < z or x > y > z:
        return 1
    else:
        return 0

def random_float(start,stop):
    """ random_float(start,stop) generate a random floating point number between start and stop """
    x = random()
    return x*abs(start-stop) + start
    
print random_float(2,6)

def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
    
print factorial(5)