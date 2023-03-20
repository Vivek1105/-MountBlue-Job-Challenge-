import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

s = input().strip()
num_error = 0
for i, char in enumerate(s):
    if i%3 == 1:
        if char != "O":
            num_error +=1
    else:
        if char != "S":
            num_error +=1
            
print(num_error)
        
