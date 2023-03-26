import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    length = 0
    while (n):
        n >>= 1
        length += 1
    return(length)
    
    # Write your code here

n = int(input().strip())
st = '{0:b}'.format(n)
elev = 0
#print(st)
for v in st:
    if(v == '0'):
        elev += 1
if(n == 0):
    elev -= 1
print(1<<elev)
