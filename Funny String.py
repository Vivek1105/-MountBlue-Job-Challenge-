#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

str1 = []
for line in sys.stdin:
    str1.append(line.strip())
    
for i in str1[1:]:
    s = i
    r = i[::-1]
    funny = True
    for j in range(1,len(i)):
        if abs(ord(s[j]) -ord(s[j-1])) != abs(ord(r[j]) -  ord(r[j-1])):
            funny = False
            break
    if funny:
        print("Funny")
    else:
        print("Not Funny")
