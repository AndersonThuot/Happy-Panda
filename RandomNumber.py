# NAME OF AUTHOR:  Anderson Thuot
# NAME OF THE PROGRAM:  Q2 range
# DATE OF CREATION:  2022-06-09
# PURPOSE OF PROGRAM:  take in 2 numbers and spit out one in between
import random
cat1 = 0
cat2 = 0
cat3 = 0
# VARIABLE DEFINITION
cat1 = int(input("Enter random number here: "))
cat2 = int(input("Enter another random number higher than the last one: "))

# INPUT 
cat3 = random.randint(cat1, cat2)
print("Your random number is: " + str(cat3)) 