# python
n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
for i in range(0,n-2):
    x = a[n-1-i]
    y = a[n-2-i]
    z = a[n-3-i]
    if y + z > x:
        print(str(z) + " "+ str(y) + " " + str(x))
        exit()
print(-1)


