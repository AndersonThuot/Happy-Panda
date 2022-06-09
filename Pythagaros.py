# NAME OF AUTHOR:  Anderson Thuot
# NAME OF THE PROGRAM:  Q1Pythagros
# DATE OF CREATION:  2021-05-17
# PURPOSE OF PROGRAM:  

# VARIABLE DEFINITION
a = 0
b = 0
c = 0
# INPUT
import math
from math import sqrt

print("Please enter sides a + b:")

a = int(input("a = "))
b = int(input("b = "))
c = sqrt(a**2 + b**2)

print("The side of your triangle is = " , c )
