from collections import deque
import sys
input=sys.stdin.readline

q=deque()

for _ in range(int(input())):
    temp=list(map(int,input().split()))
    c=temp[0]
    if c==1:
        q.appendleft(temp[1])
    elif c==2:
        q.append(temp[1])
    elif c==3:
        if q: print(q.popleft())
        else: print(-1)
    elif c==4:
        if q: print(q.pop())
        else: print(-1)
    elif c==5: print(len(q))
    elif c==6: print(1-int(bool(q)))
    elif c==7:
        if q: print(q[0])
        else: print(-1)
    elif c==8:
        if q: print(q[-1])
        else: print(-1)