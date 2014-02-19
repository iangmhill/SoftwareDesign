# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 13:36:17 2014

@author: ihill
"""

def sum_of_squares(n):
    sumSquares = 0
    for x in range(1,n+1):
        print x
        sumSquares += x**2
        #print sumSquares
    return sumSquares


def filter_out_negative_numbers(L):
    return [x for x in L if x >= 0]



def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
    
print fibonacci(10)