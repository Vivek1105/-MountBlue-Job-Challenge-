n = int( input() )
ar = [ int(v) for v in input().split() ]

count = [0]*100
for item in ar:
    count[item] += 1

for i in range(100):
    if count[i] > 0:
        print( " ".join( [str(i)]*count[i] ), end=" " )
