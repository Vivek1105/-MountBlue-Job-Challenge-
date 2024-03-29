
n,k = map(int,input().strip().split())
c = [int(s) for s in input().strip().split()]
print(100-n//k-2*sum([c[i] for i in range(0,n,k)]))

# C++
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;


int main(){
    int n;
    int k;
    cin >> n >> k;
    vector<int> c(n);
    for(int c_i = 0;c_i < n;c_i++){
       cin >> c[c_i];
    }
    
    int e = 100;
    int cur = 0;
    while (true) {
        cur += k;
        cur %= n;
        if (c[cur]) e-= 2;
        e--;
        if (cur == 0) break;
    }
    cout << e << endl;
    return 0;
}

# JAVA
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int c[] = new int[n];
        for(int c_i=0; c_i < n; c_i++){
            c[c_i] = in.nextInt();
        }
        int curr = 0;
        int Energy = 100;
        while(curr < n ){
            Energy--;
            if(c[curr]==1)
                Energy-=2;
            curr += k;
        }
        System.out.println(Energy);
    }
    
}
