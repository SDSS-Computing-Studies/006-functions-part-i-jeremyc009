#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""


def numSolutions(a,b,c):
    # inputs:
    # float a
    # float b
    # float c
    # Description:
    #
    # return 0, 1 or 2
    import math
    if ((b**2)-(4*a*c))<0:
        return 0
    disc=((b**2)-(4*a*c))**0.5
    if disc==0:
        return 1
    if disc>0:
        return 2

def solutions(a,b,c):
    #inputs:
    # float a
    # float b
    # float c
    # Desription:
    #
    # return tuple of float solution1 and float solution2
    coord=()
    x = (-b + ((b**2 - 4 * a * c)**0.5)) / (2*a)
    y=  (-b - ((b**2 - 4 * a * c)**0.5)) / (2*a)
    sols=numSolutions(a,b,c)
    if sols==0:
        return 0
    elif sols==1 or sols==2:
        coord=(x,y)
        return coord
    

def title():
    # inputs none
    # return str of All the title and instructions on one line
    ti1="This is a function to find the solutions of a quadratic function. Input three numbers (a,b and c), to find the solutions of a function of the form ax^2+bx+c=0"
    return ti1

def main():
    # Display Title and Instructions
    print( title() )
    # Your code and function calls should go here
    a=float(input("Enter the first number: "))
    b=float(input("Enter the second number: "))
    c=float(input("Enter the third number: "))
    num1=numSolutions(a,b,c)
    roots=solutions(a,b,c)

    if num1==0:
        print("There are no real solutions.")
    elif num1==1:
        print("There is one solution, x="+str(roots[0]))
    elif num1==2:
        print("There are two solutions, x="+str(roots[0])+" and x="+str(roots[1]) +".")



main()