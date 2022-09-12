from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append(start)
    visited[start[0]][start[1]]=1
    answer=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]!='X' and not visited[nx][ny]:
                visited[nx][ny]=1
                if board[nx][ny]=='P':answer+=1
                q.append((nx,ny))
    return answer

n,m=map(int,input().split())
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='I':
            start=(i,j)
            x[j]='O'
    board.append(x)
visited=[[0]*m for i in range(n)]
answer=sol()
print(answer) if answer else print('TT')
