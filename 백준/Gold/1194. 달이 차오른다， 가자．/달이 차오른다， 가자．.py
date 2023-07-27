from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def bfs():
    q=deque()
    q.append(start)
    visited[start[0]][start[1]][0]=1
    t=0
    while q:
        for _ in range(len(q)):
            x,y,key = q.popleft()
            if board[x][y]=='1': return t
            for i in range(4):
                nx,ny=x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<m and visited[nx][ny][int(key,2)]==0:
                    visited[nx][ny][int(key,2)]=1
                    if board[nx][ny]=='.' or board[nx][ny]=='1':
                        q.append((nx,ny,key))
                    elif board[nx][ny].islower():
                        if board[nx][ny]=='a':temp='1'+key[1:]
                        elif board[nx][ny]=='b':temp=key[:1]+'1'+key[2:]
                        elif board[nx][ny]=='c':temp=key[:2]+'1'+key[3:]
                        elif board[nx][ny]=='d':temp=key[:3]+'1'+key[4:]
                        elif board[nx][ny]=='e':temp=key[:4]+'1'+key[5]
                        elif board[nx][ny]=='f':temp=key[:5]+'1'
                        q.append((nx,ny,temp))
                    elif board[nx][ny].isupper():
                        if board[nx][ny]=='A' and key[0]=='1':q.append((nx,ny,key))
                        elif board[nx][ny]=='B' and key[1]=='1':q.append((nx,ny,key))
                        elif board[nx][ny]=='C' and key[2]=='1':q.append((nx,ny,key))
                        elif board[nx][ny]=='D' and key[3]=='1':q.append((nx,ny,key))
                        elif board[nx][ny]=='E' and key[4]=='1':q.append((nx,ny,key))
                        elif board[nx][ny]=='F' and key[5]=='1':q.append((nx,ny,key))
        t+=1
    return -1

n,m=map(int,input().split())
board=[]
for i in range(n):
    x=list(input())
    for j in range(m):
        if x[j]=='0':
            start = (i,j,"000000")
            x[j]='.'
    board.append(x)
visited=[[[0]*64 for i in range(m)] for i in range(n)]
print(bfs())
