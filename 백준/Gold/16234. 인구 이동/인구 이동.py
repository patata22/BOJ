from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol(x,y):
    global done
    q=deque()
    q.append((x,y))
    populcnt=board[x][y]
    legioncnt=1
    connected=[(x,y)]
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and l<=abs(board[x][y]-board[nx][ny])<=r:
                done=False
                visited[nx][ny]=1
                q.append((nx,ny))
                connected.append((nx,ny))
                legioncnt+=1
                populcnt+=board[nx][ny]
    populafter = populcnt//legioncnt
    for x,y in connected:
        board_nxt[x][y]=populafter
    
n,l,r=map(int,input().split())

board=[list(map(int,input().split())) for i in range(n)]
done = False
t=0
while not done:
    t+=1
    done=True
    board_nxt=[[0]*n for i in range(n)]
    visited=[[0]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                visited[x][y]=1
                sol(x,y)
    board=board_nxt
                
print(t-1)
