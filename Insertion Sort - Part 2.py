def insertionSort():
    arlen = int(sys.stdin.readline())
    temp_ar = sys.stdin.readline().split()
    ar = []
    for a in temp_ar:
        ar.append(int(a))
    i = 1
    switch = False
    while(i < len(ar)):
        j = i
        switch = False
        while(ar[j] < ar[j-1] and j > 0):
            ar[j], ar[j-1] = ar[j-1], ar[j]
            switch = True
            j -= 1
        i += 1
        for num in ar:
            print(num,'',end='')
            if ar.index(num) == len(ar)-1:
                print()
                
            
insertionSort()




# JAVA CODE
import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int s = in.nextInt();
        int[] ar = new int[s];
        for(int i = 0; i < s; i++){
            ar[i] = in.nextInt();
        }
        insertionSort(ar);
    }
        
    public static void insertionSort(int[] ar){
        int a; int b;
        for(a = 0, b = a + 1; b < ar.length; a++, b++){
            int temp = ar[b];
            int i = a;
            while(i >= 0 && temp < ar[i]){
                ar[i + 1] = ar[i];
                i--;
            }
            ar[i + 1] = temp;
            for(int j = 0; j < ar.length; j++){
                System.out.print(ar[j] + " ");
            }
            System.out.print("\n");
        }
        
    }   
    
}
