#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#

if __name__ == '__main__':
    import sys
    n, k = map(int, sys.stdin.readline().strip().split())
    t = list(map(int, sys.stdin.readline().strip().split()))

    page = 0
    n_special = 0
    # Iterate over chapter
    for i in range(n):
        #print("chapter{}".format(i + 1))
        page += 1
        #print("page{}".format(page))
        # Iterate over problems in chapter
        for j in range(1, t[i] + 1):
            #print("\tproblem{}".format(j))
            if j == page:
                n_special += 1
            if j != 0 and j % k == 0 and j < t[i]:
                page += 1
                #print("page{}".format(page))

    #print("---")
    print(n_special)
