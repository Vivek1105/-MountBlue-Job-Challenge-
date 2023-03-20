#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

T = int(input())

for t in range(T):
    i_v = int(input())
    c_v = [float(i) for i in str(i_v)]
    
    total = 0
    for c in c_v:
        if c==0:
            continue
        if (i_v/c) % 1 ==0:
            total +=1
    print(total)
