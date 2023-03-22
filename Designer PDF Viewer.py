import sys
import string

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

w_len = len(word)
st = string.ascii_lowercase
max_h = 0

for ch in word:
    i = st.index(ch)
    max_h = max(max_h, h[i])

ans = max_h*w_len

print(ans)





# java code
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.stream.*;

public class Solution {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[] c = new int[26];
    for (int i = 0; i < 26; ++i) {
      c[i] = in.nextInt();
    }
    String w = in.next();
    int maxH = 0;
    for (char letter : w.toCharArray()) {
      if (c[letter - 'a'] > maxH) maxH = c[letter - 'a'];
    }
    System.out.println(maxH*w.length());
  }



}
