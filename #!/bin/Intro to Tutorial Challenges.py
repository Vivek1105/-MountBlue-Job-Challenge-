#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'introTutorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER V
#  2. INTEGER_ARRAY arr
#

def introTutorial(V, arr):
    return arr.index(V)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
    
    
    
    
    
#     JAVA CODE 
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
        int value = sc.nextInt();
        int cas = sc.nextInt();
        ArrayList<Integer> ar = new ArrayList<Integer>();
        for(int i = 0;i<cas; i++)
        {
            ar.add(sc.nextInt());
        }
        
        for(int n = 0; n < ar.size();n++)
        {
            if(ar.get(n) == value)
                System.out.println(n);
        }
    }
}
