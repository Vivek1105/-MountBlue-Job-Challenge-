#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    total = {}
    for i in range(len(orders)):
        total[i + 1] = sum(orders[i])
    return [item[0] for item in sorted(total.items(), key=lambda x: x[1])]

orders = []
for orders_i in range(int(input().strip())):
    orders.append([int(orders_temp) for orders_temp in input().strip().split(' ')])
print (" ".join(map(str, jimOrders(orders))))
