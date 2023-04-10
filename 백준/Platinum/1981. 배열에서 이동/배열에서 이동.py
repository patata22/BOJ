from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def bfs():
    q=deque()
    visited=[[0]*n for i in range(n)]
    q.append((0,0))
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        if x==n-1 and y==n-1:return True
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and l<=board[nx][ny]<=r:
                visited[nx][ny]=1
                q.append((nx,ny))
        
    return False


n=int(input())
board=[]
l_min,r_max=float('inf'), 0
answer=float('inf')
for i in range(n):
    x=list(map(int,input().split()))
    l_min=min(l_min,min(x))
    r_max=max(r_max,max(x))
    board.append(x)
l_max=min(board[0][0],board[n-1][n-1])
r_min=max(board[0][0],board[n-1][n-1])
l,r=l_min,r_min
while l_min<=l<=l_max and r_min<=r<=r_max:
    if bfs():
        answer=min(answer,r-l)
        l+=1
    else:r+=1


print(answer)
