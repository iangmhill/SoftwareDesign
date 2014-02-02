# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 10:56:22 2014

@author: ihill
"""

def check_fermat (a,b,c,n):
    if (a**n + b**n) == c**n and n > 2:
        print "Holy smokes, Fermat was wrong!"
    elif n <= 2:
        print "Well, that's not very exciting..."
    else:
        print "No, that doesn't work."

print "Let's see if Fermat was right!"
a = int(raw_input("a = "))
b = int(raw_input("b = "))
c = int(raw_input("c = "))
n = int(raw_input("n = "))

check_fermat(a,b,c,n)