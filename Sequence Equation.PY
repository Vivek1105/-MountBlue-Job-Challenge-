n=int(input())
fDict=dict()
fInvDict=dict()

L=input().split()
for i in range(n):
    fDict[i+1] = int(L[i])
    fInvDict[int(L[i])] = i+1
for x in range(1,n+1):
    print(fInvDict[fInvDict[x]])
    
    
    
    
# JAVA SOLUTION 
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    public static void main(String args[] ) throws Exception {
        Scanner in=new Scanner(System.in);
        int n=in.nextInt();
        int[] a=new int[n];
        for(int i=0;i<n;i++)
            a[i]=in.nextInt();
        for(int i=1;i<=n;i++){
            for(int j=0;j<n;j++){
                if(i==a[j]){
                  for(int k=0;k<n;k++)  {
                      if((j+1)==a[k])
                          System.out.println(k+1);
                  }
                }
            }
        }
    }
}



# C++ SOLUTION 
#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int, int> II;

int main() {
    #ifdef LOCAL
        freopen("Data.inp", "r", stdin);
        freopen("Data.out", "w", stdout);
    #endif

    int n, a[100];
    cin >> n;
    for (int i = 1; i <= n; ++i) cin >> a[i];

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) if (a[a[j]] == i) {
            cout << j << endl;
            break;
        }
    }

    return 0;
}
