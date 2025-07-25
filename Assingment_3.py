#Task 1: Calculate Factorial Using a Function 


#Problem Statement: Write a Python program that:
#1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2.   Returns the calculated factorial.
#3.   Calls the function with a sample number and prints the output.
a=int(input("Enter a Number:"))
def fact(a):
    if a<2:
        return (1)
    else:
        return a * (fact(a-1))
        

result= fact(5)
print("Factorial of" ,a ,"is:",result)

#Task 2: Using the Math Module for Calculations
 
#Problem Statement: Write a Python program that:
#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)
import math
a= int(input("Enter a number:"))
print("Square root:",a**2)
print("Natural logarithm:",math.log(a))
print("Sine of the number:",math.sin(a))