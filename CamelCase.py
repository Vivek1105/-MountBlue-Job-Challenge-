#!/bin/python3

import sys


s = input().strip()

count = 1
for letter in s:
    if ord(letter) <= ord('Z'):
        count += 1
print(count)



# JAVA
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String s = in.next();
        String p = s.toUpperCase();
        int l = s.length();
        int ans = 1;
        for (int i = 0; i < l; i++) {
            if (p.charAt(i) == s.charAt(i)) ans++;
        }
        
        System.out.println(ans);
    }
}

