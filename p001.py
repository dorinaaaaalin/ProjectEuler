# Question
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#   we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Input Format
# First line contains t that denotes the number of test cases. 
#  This is followed by t lines, each containing an integer n.

# Output Format
# For each test case, 
#   print an integer that denotes the sum of all the multiples of 3 or 5 below .

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sum(x for x in range(n) if(x%3==0 or x%5==0)))
