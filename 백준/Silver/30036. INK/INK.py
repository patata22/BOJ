from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def move(cmd,x,y):
   if cmd=='U': d=0
   elif cmd=='D': d=1
   elif cmd=='L': d=2
   elif cmd=='R': d=3
   nx,ny=x+dx[d],y+dy[d]
   if 0<=nx<n and 0<=ny<n and board[nx][ny]=='.': return nx,ny
   return x,y

def jump(x,y):
   now=color[jumpCount%C]
   q=deque()
   q.append((x,y))
   visited=[[0]*n for i in range(n)]
   visited[x][y]=1
   t=0
   target=[]
   while t<ink:
      for _ in range(len(q)):
         x,y=q.popleft()
         for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
               visited[nx][ny]=1
               q.append((nx,ny))
               if board[nx][ny]!='.': target.append((nx,ny))
      t+=1
   for x,y in target:
      board[x][y]=now

C,n,k=map(int,input().split())

color=list(input())
ink=0
jumpCount=0
board=[]
for i in range(n):
   temp=list(input())
   for j in range(n):
      if temp[j]=='@':
         x,y=i,j
         temp[j]='.'
   board.append(temp)

CMD=list(input())

for cmd in CMD:
   if cmd=='j': ink+=1
   elif cmd=='J':
      jump(x,y)
      jumpCount+=1
      ink=0
   else: x,y=move(cmd,x,y)


board[x][y]='@'

for i in range(n):
   print(''.join(board[i]))