dx=(-1,1,0,0)
dy=(0,0,-1,1)


def sol(x1,y1,x2,y2):
   if x1==x2 and y1==y2:
      global answer
      temp = sum([sum(board[i]) for i in range(5)])
      if temp==0: answer+=1
      return

   for i in range(4):
      nx1,ny1=x1+dx[i],y1+dy[i]
      if 0<=nx1<5 and 0<=ny1<5 and board[nx1][ny1]:
         for j in range(4):
            nx2,ny2=x2+dx[j],y2+dy[j]
            if 0<=nx2<5 and 0<=ny2<5 and board[nx2][ny2]:
               board[nx1][ny1]=0
               board[nx2][ny2]=0
               sol(nx1,ny1,nx2,ny2)
               board[nx2][ny2]=1
               board[nx1][ny1]=1
            

board=[[1]*5 for i in range(5)]
for _ in range(int(input())):
   x,y=map(int,input().split())
   board[x-1][y-1]=0
answer=0


board[0][0]=0
board[4][4]=0
sol(0,0,4,4)
print(answer)
