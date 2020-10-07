#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(flnum):
    value=flnum%2
    result=(value==1 or value==0)
    return result
num=isInteger(-3)
print(num)