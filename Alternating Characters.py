def f(s):
    return sum(1 for c1, c2 in zip(s, s[1:]) if c1 == c2)

t = int(input())
for _ in range(t):
    print(f(input()))


c++

#include <iostream>
#include <string>

using namespace std ;

int main()
{
    int test_cases;
    cin >> test_cases ;
    string str;
    int count  ;
    int j ;
    char prev ;
    for ( int i =0 ; i < test_cases ;i++)
    {
        cin >> str ;
        j = 1; prev = str[0]; count = 0 ; 
        while((int)str[j]!=0)
        {
            if(str[j] == prev)
                count ++ ;
            else
                prev = str[j] ;
            j++ ;
        }
        cout << count << endl ;
    }
    return 0 ;
}
