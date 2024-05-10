from collections import deque

def sol(a,b):
    q=deque()
    q.append(line[a])
    visited=[0]*100
    visited[a]=1
    while q:
        x,y,now = q.popleft()
        if now==b: return 1
        for x2,y2,to in line:
            if not visited[to] and (x2<x<y2 or x2<y<y2):
                visited[to]=1
                q.append((x2,y2,to))
        
    return 0


n=int(input())
line=[]
unused=0
for _ in range(n):
    cmd,a,b=map(int,input().split())
    if cmd==1:
        line.append((a,b,unused))
        unused+=1
    elif cmd==2:
        print(sol(a-1,b-1))
