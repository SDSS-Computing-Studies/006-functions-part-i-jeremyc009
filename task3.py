#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""

def perimeter(num):
    coun=len(num)
    b=0
    for i in range(0,coun):
        a=num[i]
        c=a+b
        b=c     
    return c    

x=perimeter([9,8,6,5.5])
print(x)
