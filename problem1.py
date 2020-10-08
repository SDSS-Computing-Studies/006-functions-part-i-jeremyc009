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
    mSide=0
    if c==True and a>b:
        mSide=math.sqrt(a**2 - b**2)
        return mSide
    elif c==True and b>a:
        mSide=math.sqrt(b**2 - a**2)
        return mSide
    elif c==False:
        mSide=0
        mSide=math.sqrt(a**2 + b**2)
        return mSide
print(hypotenuse(13,5,True))