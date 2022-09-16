from collections import deque

def sol():
    q=deque()
    q.append((s,t))
    visited[s][t]=1
    T=0
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            if x==y:
            
                return T
            if not visited[x+1][y]:
                visited[x+1][y]=1
                q.append((x+1,y))
            if 2*x<=y+3 and not visited[2*x][y+3]:
                visited[x*2][y+3]=1
                q.append((2*x,y+3))
        T+=1
                

for _ in range(int(input())):
    s,t=map(int,input().split())
    visited=[[0]*200 for i in range(200)]
    print(sol())

