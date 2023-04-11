s = input()
n = 1
while n * n < len(s):
    n += 1

a = s + ' ' * (n * n - len(s))
a = [a[i:i+n] for i in range(0, n * n, n)]

print(' '.join([''.join([a[j][i] for j in range(n)]).strip() for i in range(n)]))




# java code
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int size = input.length();
        int rowSize = (int)Math.floor(Math.sqrt(size));
        int colSize = (int)Math.ceil(Math.sqrt(size));
       
        while(colSize>rowSize){
            colSize--;
            if((colSize*rowSize)<size){
                colSize++;
                break;
            }
        }
        while((colSize*rowSize)<size&&(colSize>rowSize)){
            rowSize++;
        }
        
        for(int i =0;i<colSize;i++){
            
            int row = 0;
            while(row<=rowSize-1){
                if((i+row*colSize)<size)
                {
                    System.out.print(input.charAt(i+row*colSize)); 
                     row++;
                }     else{
                    break;
                }        
             
            }
            System.out.print(" ");
        }
    }
}
