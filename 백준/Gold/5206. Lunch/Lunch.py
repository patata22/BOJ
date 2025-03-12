from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def meetingToStart(x,y):
    q=deque()
    q.append((x,y))
    visited=[[0]*m for i in range(n)]
    visited[x][y]=1
    result=0
    cnt=0
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and board[nx][ny]=='.' and not visited[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    if (nx,ny) in start:
                        cnt+=1
                        result+=t
        t+=1

    if cnt==len(start): return result
    else: return float('inf')
                        
def meetingToRes(x,y):
    q=deque()
    q.append((x,y))
    visited=[[0]*m for i in range(n)]
    visited[x][y]=1
    t=0
    result=float('inf')
    while q:
        t+=len(start)
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]!='X':
                    visited[nx][ny]=1
                    if board[nx][ny]=='R':
                        result=min(result, resToStart(nx,ny)+t)
                    else:q.append((nx,ny))

    return result

def resToStart(x,y):
    q=deque()
    q.append((x,y))
    visited=[[0]*m for i in range(n)]
    visited[x][y]=1
    cnt=0
    result=0
    t=1
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]=='.':
                    visited[nx][ny]=1
                    q.append((nx,ny))
                    if (nx,ny) in start:
                        cnt+=1
                        result+=t
        t+=1
    if cnt==len(start): return result
    else: return float('inf')
                
for tt in range(int(input())):
    n,m=map(int,input().split())
    board=[]
    start=set()
    meeting=[]
    restaurant=[]
    for i in range(n):
        temp=list(input())
        for j in range(m):
            if temp[j]=='S':
                start.add((i,j))
                temp[j]='.'
            elif temp[j]=='M':
                meeting.append((i,j))
                temp[j]='.'
            elif temp[j]=='R':
                restaurant.append((i,j))
        board.append(temp)
    answer = float('inf')
    for x,y in meeting:
        mts = meetingToStart(x,y)
        mtr = meetingToRes(x,y)
        #print(x,y,mts,mtr)
        answer=min(answer,mts+mtr)

    print(f'Data Set {tt+1}:')
    print('Impossible') if answer==float('inf') else print(answer)
