from collections import deque
import sys
input=sys.stdin.readline

def isCover(bottom,top):
    r1,c1,r2,c2=bottom
    r,c = r1,c2
    r1,c1,r2,c2=top
    return r1<=r<=r2 and c1<=c<=c2

n=int(input())
square=[tuple(map(int,input().split())) for i in range(n)]
used=[0]*n
q=deque()
q.append(0)
used[0]=1
while q:
    now=q.popleft()
    for i in range(now+1,n):
        if not used[i] and isCover(square[now],square[i]):
            used[i]=1
            q.append(i)

print(sum(used))