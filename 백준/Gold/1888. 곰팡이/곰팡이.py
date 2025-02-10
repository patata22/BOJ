from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
   q=deque()
   for i in range(n):
      for j in range(m):
         if board[i][j]:
            q.append((i,j))
   t=0
   if check(): return t
   while q:
      t+=1
      temp={}
      for _ in range(len(q)):
         x,y=q.popleft()
         k=board[x][y]
         for nx in range(x-k,x+k+1):
            for ny in range(y-k,y+k+1):
               if 0<=nx<n and 0<=ny<m and board[nx][ny]<k:
                  if (nx,ny) in temp: temp[(nx,ny)]=max(temp[(nx,ny)],k)
                  else: temp[(nx,ny)]=k
      for x,y in temp:
         board[x][y]=temp[(x,y)]
         q.append((x,y))
                  
      if check(): return t

def check():
   cnt=0
   visited=[[0]*m for i in range(n)]
   for i in range(n):
      for j in range(m):
         if board[i][j] and not visited[i][j]:
            cnt+=1
            q=deque()
            q.append((i,j))
            visited[i][j]=1
            while q:
               x,y=q.popleft()
               for i in range(4):
                  nx,ny=x+dx[i],y+dy[i]
                  if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                     visited[nx][ny]=1
                     q.append((nx,ny))
               
   return cnt==1      
            
n,m=map(int,input().split())
board=[list(map(int,input())) for i in range(n)]
print(sol())
