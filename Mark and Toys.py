#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

n, k = map(int, input().split())
prices = list(sorted(map(int, input().split())))
toys = 0

for price in prices:
    if price <= k:
        k -= price
        toys += 1
    else:
        break

print(toys)



# Another Approach 
def maximumToys(prices, k):
    items = 0
    prices.sort()
    for p in prices:
        if p <= k:
            items += 1
            k -= p
        else:
            break
    return items

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
