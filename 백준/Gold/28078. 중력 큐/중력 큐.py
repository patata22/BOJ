import sys
input=sys.stdin.readline
from collections import deque

def gravity():
    global b
    if d==0:
        while q and q[-1]!=-1:
            b-=1
            q.pop()
    elif d==2:
        while q and q[0]!=-1:
            b-=1
            q.popleft()
            
d=1
b=0
w=0
q=deque()

for _ in range(int(input())):
    cmd=input().rstrip().split()
    if cmd[0]=='push':
        if cmd[1]=='b':
            q.append(1)
            b+=1
        elif cmd[1]=='w':
            q.append(-1)
            w+=1
        gravity()
    elif cmd[0]=='count':
        if cmd[1]=='b':print(b)
        else:print(w)
    elif cmd[0]=='pop':
        if q:
            if q[0]==1:
                q.popleft()
                b-=1
            else:
                q.popleft()
                w-=1
            gravity()
    elif cmd[0]=='rotate':
        if cmd[1]=='r': d=(d+1)%4
        else: d=(d-1)%4
        gravity()