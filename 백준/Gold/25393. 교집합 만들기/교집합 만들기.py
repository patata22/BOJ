import sys
input=sys.stdin.readline

left=[-1]*1000001
right=[float('inf')]*1000001
pair=set()
for _ in range(int(input())):
    l,r=map(int,input().split())
    pair.add((l,r))
    left[l] = max(left[l],r)
    right[r] = min(right[r],l)

for _ in range(int(input())):
    l,r=map(int,input().split())
    if (l,r) in pair: print(1)
    elif left[l]>r and right[r]<l: print(2)
    else: print(-1)
        
