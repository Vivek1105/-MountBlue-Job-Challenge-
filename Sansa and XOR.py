T = int(input())
for _ in range(T):
    N = int(input())
    ar = [int(i) for i in input().split()]
    
    result = 0
    count = 0
    for i in range(N):
        count += N - 2*i
        if (count) % 2 == 1:
            result = result ^ ar[i]
    print(result)
