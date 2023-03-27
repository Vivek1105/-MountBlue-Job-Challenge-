#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range (1,101):
    if all(i%x == 0 for x in a) and all(x%i == 0 for x in b):
        ans +=1
print(ans)
