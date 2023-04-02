import sys

N = int(sys.stdin.readline())

a = list(sys.stdin.readline().split())
for index, item in enumerate(a):
    a[index] = int(item)

a = sorted(a)

count = 0
i = 0
while i < N:
    temp = int(a[i]) + 4
    count+=1
    while i < N and int(a[i]) <= temp:
        i+=1

print (count
