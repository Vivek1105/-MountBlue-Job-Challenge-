t = int(input())
for _ in range(t):
    parts = list(map(int, input().split(' ')))
    # print('parts', parts)
    print((parts[1] + parts[2] - 2) % parts[0] + 1)

    
#     C++
#include <iostream>
  
using namespace std;

bool isOk(int x, int mod) {
    int n = x;
    int m = 0;
    while (x > 0) {
        m = m * 10 + x % 10;
        x /= 10;
    }
    int delta = abs(n - m);
    delta %= mod;
    return (delta == 0);
}

int main() {
    int l, r, k;
    cin >> l >> r >> k;
    int ans = 0;
    for (int i = l; i <= r; i++) {
        if (isOk(i, k)) {
            ++ans;
        }
    }
    cout << ans << endl;
    return 0;
}
