import sys
sys.setrecursionlimit(10**6)

dx=(-1,1,0,0)
dy=(0,0,-1,1)
D={'U':0, 'D':1, 'L':2, 'R':3}


def dfs(x,y):
    visited[x][y]=1
    d=D[board[x][y]]
    nx,ny= x+dx[d], y+dy[d]
    if 0<=nx<n and 0<=ny<m:
        if not visited[nx][ny]:
            answer[x][y]=dfs(nx,ny)
        elif visited[nx][ny]:   
            answer[x][y]=answer[nx][ny]
    else:
        answer[x][y]=1
    return answer[x][y]


n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
visited=[[0]*m for i in range(n)]
answer=[[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            dfs(i,j)
            
a=0
for i in range(n):
    a+=sum(answer[i])
print(a)
