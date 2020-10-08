#! python3
"""
Create a function called factors()
Input parameter is a positive integer
Output is a sorted list containing all of the factors of that number.
Note: A Factor is a positive integer that can be evenly divided
into another number.
Example: The factors of 10 are 1, 2, 5, 10
(2 points)
"""

def factors(num):
    numList=[]
    for i in range(1,num+1):
        if num%i==0:
            numList.append(i)
    numList.sort()
    return numList
print(factors(24))