from collections import deque
import sys
input=sys.stdin.readline

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
   q=deque()
   water=[[1]*(m+1) for i in range(n+1)]
   visited=[[0]*(m+1) for i in range(n+1)]
   for _ in range(int(input())):
      x,y=map(int,input().split())
      water[x][y]=0
      q.append((x,y))

   while q:
      x,y=q.popleft()
      for i in range(4):
         nx,ny=x+dx[i],y+dy[i]
         if 0<nx<=n and 0<ny<=m and not visited[nx][ny] and board[nx][ny]>=board[x][y]:
            visited[nx][ny]=1
            water[nx][ny]=0
            q.append((nx,ny))
            
   for i in range(n+1):
      for j in range(1,m+1):
         water[i][j]+=water[i][j-1]

   for j in range(m+1):
      for i in range(1,n+1):
         water[i][j]+=water[i-1][j]

   answer=0
   for i in range(h,n+1):
      for j in range(w,m+1):
         if water[i][j]-water[i][j-w]-water[i-h][j]+water[i-h][j-w]==0:
            answer+=1
         
   return answer

n,m=map(int,input().split())
h,w=map(int,input().split())

board=[]
board.append([0]*(m+1))
for _ in range(n):
   board.append([0]+list(map(int,input().split())))

print(sol())