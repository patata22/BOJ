from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    q=deque()
    q.append(coin)
    visited.add((coin[0],coin[1],coin[2],coin[3]))
    t=0
    while q and t<=10:
        for _ in range(len(q)):         
            x1,y1,x2,y2=q.popleft()
            #print(x1,y1,x2,y2)
            cnt=0
            if (x1 in (0,n-1) or y1 in (0,m-1)):cnt+=1
            if (x2 in (0,n-1) or y2 in (0,m-1)):cnt+=1
            if cnt==1:
                return t
            if cnt!=2:
                for d in range(4):
                    nx1,ny1,nx2,ny2=x1+dx[d],y1+dy[d],x2+dx[d],y2+dy[d]
                    if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
                        if board[nx1][ny1]=='#':nx1,ny1=x1,y1
                        if board[nx2][ny2]=='#':nx2,ny2=x2,y2
                        if (nx1,ny1,nx2,ny2) not in visited:
                            visited.add((nx1,ny1,nx2,ny2))
                            q.append((nx1,ny1,nx2,ny2))
        t+=1
    return -1
                    
n,m=map(int,input().split())
board=[]
board.append(['.']*(m+2))
for i in range(n):
    board.append(['.']+list(input())+['.'])
board.append(['.']*(m+2)) 
coin=[]
for i in range(n+2):
    for j in range(m+2):
        if board[i][j]=='o':
            board[i][j]='.'
            coin.append(i)
            coin.append(j)
n+=2
m+=2
visited=set()
print(sol())