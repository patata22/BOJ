from collections import deque
import sys
input=sys.stdin.readline

n,m=map(int,input().split())
answer=[]
ice = [(i,x) for i,x in enumerate(map(int,input().split()))]
ice.sort(key= lambda x: (x[1],-x[0]))
Rev=False
while ice:
    now = ice[-1][1]
    q=deque()
    while ice and ice[-1][1] ==now:
        q.append(ice.pop())
    while q:
        if Rev:
            i,x = q.pop()
        else:
            i,x = q.popleft()
        answer.append(i+1)
        if not x%7: Rev= not Rev
print(*answer[:m], sep = '\n')