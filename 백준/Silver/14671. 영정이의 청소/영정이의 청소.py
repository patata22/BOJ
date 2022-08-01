from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,-1,1,1)
dy=(-1,1,-1,1)

def sol():
    q=deque()
    for _ in range(k):
        x,y=map(int,input().split())
        q.append((x-1,y-1))
        visited[x-1][y-1][0]=1
        count[0]+=1
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny][t]:
                    visited[nx][ny][t]=1
                    count[t]+=1
                    q.append((nx,ny))
                    
        t=1-t


n,m,k=map(int,input().split())
visited=[[[0]*2 for i in range(m)] for i in range(n)]

count=[0,0]
sol()
print('YES') if n*m in count else print('NO')
