#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

from math import *

def get_turn(turns):
    return "Richard" if turns % 2 == 0 else "Louise"

def npot(x):
    exp = floor(log(x, 2))
    r = int(pow(2, exp))
    return r
    
def run_game(n):
    turns = 0
    while(n > 1):
        np = npot(n)
        if np == n:
            n >>= 1
        else:
            n -= np
        turns += 1
    print(get_turn(turns))

t = int(input())
for i in range(t):
    n = int(input())
    run_game(n)
    
    
    
    
#   JAVA CODE 
import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int numTests = in.nextInt();
        for (int i = 0; i < numTests; ++i) {
            findWinner(in);
        }
    }
    
    private static void findWinner(Scanner in) {
        String counterAsString = in.next();
        BigInteger counter = new BigInteger(counterAsString);
        int bits = counter.bitLength();
        int moves = -1;
        for (int i = 0; i < bits; ++i) {
            if (!counter.testBit(i)) {
                ++moves;
            } else {
                moves += counter.bitCount();
                break;
            }
        }
        if (moves % 2 == 0) {
            System.out.println("Richard");
        } else {
            System.out.println("Louise");
        }
    }
}
