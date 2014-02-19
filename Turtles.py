# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:44:44 2014

@author: ihill
"""
from swampy.TurtleWorld import *
from math import pi
from random import random
world = TurtleWorld()
bob = Turtle()
bob.delay = 0

def my_square(turtle,x,y):
    turtle.x = x
    turtle.y = y
    turtle.heading = 90
    for n in range(4):
        fd(turtle,100)
        rt(turtle)
    wait_for_user()

def my_regular_polygon(turtle,x,y,n,length):
    turtle.x = x
    turtle.y = y
    turtle.heading = 180.0-(360.0/n)
    for u in range(n):
        fd(turtle,length)
        rt(turtle,360.0/n)
    #wait_for_user()

def my_circle(turtle,x,y,r):
    length = (2*pi*r)/100
    my_regular_polygon(turtle,x,y-r,100,length)

def draw_snowflake_side(turtle, l, level):
    if level <= 1:
        fd(turtle,l)
        rt(turtle,60)
        fd(turtle,l)
        lt(turtle,120)
        fd(turtle,l)
        rt(turtle,60)
        fd(turtle,l)
    else:
        draw_snowflake_side(turtle,l/3.0,level-1)
        rt(turtle,60)
        draw_snowflake_side(turtle,l/3.0,level-1)
        lt(turtle,120)
        draw_snowflake_side(turtle,l/3.0,level-1)
        rt(turtle,60)
        draw_snowflake_side(turtle,l/3.0,level-1)

def draw_snowflake(turtle,l,level,sides):
    #turtle.heading = 180.0-(360.0/sides)
    for n in range(sides):
        draw_snowflake_side(turtle, l, level)
        rt(turtle,360.0/sides)
        
def recursive_tree(turtle, branch_length, level):
    tolerance = 1
    q = random()*tolerance + (1-tolerance*.5)
    if level <= 1:
        fd(turtle,branch_length*q)
    else:
        q = random()*tolerance + (1-tolerance*.5)
        fd(turtle,branch_length*q)
        
        scott = Turtle()
        scott.x = turtle.x
        scott.y = turtle.y
        scott.heading = turtle.heading
        scott.delay = turtle.delay
        lt(scott,30*q)
        recursive_tree(scott,branch_length*0.6*q,level-1)
        scott.undraw()
        
        bk(turtle,(branch_length/3.0)*q)
        q = random()*tolerance + (1-tolerance*.5)
        
        william = Turtle()
        william.x = turtle.x
        william.y = turtle.y
        william.heading = turtle.heading
        william.delay = turtle.delay
        rt(william,40*q)
        recursive_tree(william,branch_length*0.64*q,level-1)
        william.undraw()
        
        fd(turtle,branch_length*0.1)
        q = random()*tolerance + (1-tolerance*.5)
        
        ben = Turtle()
        ben.x = turtle.x
        ben.y = turtle.y
        ben.heading = turtle.heading
        ben.delay = turtle.delay
        lt(ben,56*q)
        recursive_tree(ben,branch_length*0.57*q,level-1)
        ben.undraw()    

#my_circle(bob,0,0,50)
#my_square(bob,bob.x-100,bob.y)
#draw_snowflake_side(bob,50,4)
bob.x = 0
bob.y = -100
bob.heading = 90
#draw_snowflake(bob,50,3,7)
recursive_tree(bob,100,8)
wait_for_user()