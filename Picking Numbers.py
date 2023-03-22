import sys

def count(n, a):
    return len(list(filter( (lambda x: x==n), a)))

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

mi = min(a)
ma = max(a)
maxCount = -1
if mi == ma:
    print(len(a))
else:
    for i in range(mi, ma):
            c = count(i, a) + count(i+1, a)
            if c > maxCount:
                maxCount = c
            
    print(maxCount)
    
    
   

# Java code 
import java.io.*;
import java.util.*;

public class Solution
{
	public static void main(String[] args)
	{
		Scanner readIn = new Scanner(System.in);
		
		int n = readIn.nextInt();
		int[] frequencie = new int[100];
		for(int ii = 0; ii < n; ii++)
			frequencie[readIn.nextInt()]++;
		
		int out = Integer.MIN_VALUE;
		for(int ii = 0; ii < frequencie.length - 1; ii++)
			out = frequencie[ii] + frequencie[ii + 1] > out ? frequencie[ii] + frequencie[ii + 1] : out;
		
		System.out.println(out);
	}
}

