#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side
(2 points)
"""
def hypotenuse(a,b,c):
    import math
    if c==True:
        mSide=0
        lSide=0
        sSide=0
        if a>b:
            a=lSide
            b=sSide
        elif b>a:
            b=lSide
            a=sSide
        mSide=math.sqrt(lSide**2 - sSide**2)
        return mSide
    elif c==False:
        mSide=0
        mSide=math.sqrt(a**2 + b**2)
        return mSide
