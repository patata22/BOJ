from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)
D={'W':0,'S':1,'A':2,'D':3}
RD={0:'W',1:'S',2:'A',3:'D'}
def sol(x,y,t):
    global finished
    if finished: return
    if x==ex and y==ey:
        finished=True
        return
    if t>=N: return
    for d in cmd[t]:
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.':
            sol(nx,ny,t+1)
            if finished:
                answer.append(RD[d])
                return

n,m=map(int,input().split())
board=[]
for i in range(n):
    temp=list(input())
    for j in range(m):
        if temp[j]=='D':
            temp[j]='.'
            sx,sy=i,j
        elif temp[j]=='Z':
            temp[j]='.'
            ex,ey=i,j
    board.append(temp)

N=int(input())
cmd=[tuple(map(lambda x: D[x], input().split())) for i in range(N)]


answer=[]
finished=False
sol(sx,sy,0)
if finished:
    print('YES')
    print(''.join(answer[::-1]))
else: print('NO')
          
