#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""

def distance(coord1, coord2):
    a=coord1[0]
    b=coord1[1]
    c=coord2[0]
    d=coord2[1]
    x=a-c
    y=b-d
    dist=(x**2 + y**2)**(1/2)
    dist=round(dist,3)
    return dist
num=distance((2,3),(5,6))
print(num)