def sup_digits(x,k):
    a = digsum(x)
    return sup_digit(str(int(a)*k))

def sup_digit(x):
    if len(x) <= 1:
        return x
    else:
        return sup_digit( digsum(x) )

def digsum(x):
    return str(sum((int(i) for i in list(x))))


n, k = input().split()
print( sup_digits(n, int(k)))




# JAVA CODE 
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Solution s = new Solution();
        Scanner sc = new Scanner(System.in);
        
        String str_n = sc.next();
        int k = sc.nextInt();
        
        int pSum = Integer.parseInt(s.supdig(str_n));
        pSum *= k;
                        
        String sup = Integer.toString(s.supdig(pSum));
        
        System.out.println(sup);
    }
    
    String supdig(String n) {
        if(n.length() == 1) return n;
        else {
            int np = 0;
            
            for(int i = 0; i < n.length(); i++) {
                np += Character.getNumericValue( n.charAt(i) );    
            }
            
            return supdig(Integer.toString(np));
        }       
    }
    
    int supdig(int n) {
        if(n / 10 == 0) return n;
        else {
            int r = 0;
            
            while(n > 0) {
                r += n % 10;
                n /= 10;
            }
            
            return supdig(r);
        }
    }
}
