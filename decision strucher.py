# Placing a hash tag in front of a line will make the line not execute 
# line not execute 
# This is referred to as "comment"
from email._header_value_parser import Comment

print("Hello World!")

'''
Line 1 of block Comment
line 2 of block comment 
line 3 of block comment 
'''

"""

Line 1 of block Comment
line 2 of block comment 
line 3 of block comment 
"""

""" A condition is a comparison.
Conditions evaluate  a  boolean  value  to be true or false .
If condition is true, the following  block of code  will run.
A block of code will be intended.

COMPARISONS :
>  Greater than 
< Less than 
>= Greater than or equal to
<= Less than or equal to
== Equal to
!= Not equal

"""

mark = int(input("Please enter your test mark"))


if mark > 49 and mark < 70:
    print("You passed!")
    
if mark >= 90: 
    print("You aced!")
    
if mark == 100:
    print("100% :)")
    
elif mark >= 70:
    print("You got a B goodjob!")
    
elif mark >= 60:
    print("stupid got a C")

elif mark >=50:
    print("You a lucky mf")

elif mark >= 49:
    print("L for loser")
    
if (mark > 100 or mark <0):
    print("You're lying")
    
