from collections import deque

dx=(-1,1)


def bfs(x,y,l,r):
    global answer
    q=deque()
    q.append((x,y,l,r))
    visited[x1][y1]=1
    while q:
        x,y,l,r=q.popleft()
        for i in range(2):
            nx=x
            while 0<=nx+dx[i]<n:
                nx+=dx[i]
                if board[nx][y]=='1':break
                if visited[nx][y]==0:
                    answer+=1
                    visited[nx][y]=1
                    q.append((nx,y,l,r))
        if r>0 and y<m-1 and visited[x][y+1]==0 and board[x][y+1]!='1':
            answer+=1
            visited[x][y+1]=1
            q.append((x,y+1,l,r-1))
        if l>0 and 0<y and visited[x][y-1]==0 and board[x][y-1]!='1':
            answer+=1
            visited[x][y-1]=1
            q.append((x,y-1,l-1,r))
            
                
                    
        
answer=1
n,m=map(int,input().split())
l,r=map(int,input().split())
visited=[[0]*m for i in range(n)]
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='2': x1,y1=i,j
    board.append(x)
bfs(x1,y1,l,r)
print(answer)
