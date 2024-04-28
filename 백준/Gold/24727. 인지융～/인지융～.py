from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)



def cut():
    q=deque()
    q.append((0,0))
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=1
                if board[nx][ny]==1: q.append((nx,ny))
                
def fill():
    if visited[-1][-1]:return 0
    q=deque()
    cnt2=0
    q.append((n-1,n-1))
    board[n-1][n-1]=2
    visited[n-1][n-1]=1
    cnt2=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                board[nx][ny]=2
                cnt2+=1
                if cnt2==b: return cnt2
    return cnt2
n=int(input())
a,b=map(int,input().split())
board=[[0]*n for i in range(n)]
visited=[[0]*n for i in range(n)]
cnt1=0
for i in range(n):
    if cnt1==a: break
    for j in range(n):
        board[i][j]=1
        cnt1+=1
        if cnt1==a: break

cut()
cnt2=fill()


if cnt1==a and cnt2==b:
    print(1)
    for i in range(n):
        print(*board[i],sep='')
else:
    print(-1)
