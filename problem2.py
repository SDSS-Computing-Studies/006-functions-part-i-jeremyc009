#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(a,b,c,d):
    x=a-c
    y=b-d
    dist=(x**2 + y**2)**(1/2)
    return dist

