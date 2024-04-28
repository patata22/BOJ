import heapq
from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def fillA():
    row=0
    cnt1=0
    while cnt1<a and row<2*n+1:
        x=row
        y=0
        while 0<=x:
            if 0<=x<n and 0<=y<n:
                cnt1+=1
                board[x][y]=1
                if cnt1==a: return cnt1
            x-=1
            y+=1
        row+=1
    return cnt1
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
    
def fillB():
    q=deque()
    for i in range(n-1,-1,-1):
        if q: break
        for j in range(n-1,-1,-1):
            if not visited[i][j]:
                board[i][j]=2
                visited[i][j]=1
                q.append((i,j))
                break
    if not q: return 0
    cnt2=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                visited[nx][ny]=1
                board[nx][ny]=2
                cnt2+=1
                q.append((nx,ny))
                if cnt2==b: return cnt2
    return cnt2
                
    
n=int(input())
a,b=map(int,input().split())
board=[[0]*n for i in range(n)]
visited=[[0]*n for i in range(n)]

cnt1=fillA()
cut()
cnt2=fillB()
if cnt1==a and cnt2==b:
    print(1)
    for i in range(n):
        print(*board[i],sep='')
else: print(-1)
