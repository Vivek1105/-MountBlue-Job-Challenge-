#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input())
arr = list(map(int,input().split()))
freq = [0]*100
for i in arr:
    freq[i] = freq[i]+1
print(" ".join(map(str,freq)))
