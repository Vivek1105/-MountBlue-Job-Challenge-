from collections import Counter

k1 = input()
c1 = Counter(map(int, input().split()))
k2 = input()
c2 = Counter(map(int, input().split()))

if k1 > k2:
    c2, c1 = c1, c2
    
l = []
for k in c2.keys():
    if k not in c1 or c1[k] < c2[k]:
        l.append(k)
        
print(' '.join(map(str, sorted(l))))
