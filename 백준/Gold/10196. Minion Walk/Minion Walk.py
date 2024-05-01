from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def sol():
    if board[0][0]=='X': return
    q=deque()
    q.append((0,0))
    visited[0][0]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and board[nx][ny]=='O':
                visited[nx][ny]=1
                q.append((nx,ny))

def printResult(i):
    x=board[i]
    temp=['|']
    for j in range(m):
        if x[j]=='X': temp.append(' X |')
        elif visited[i][j]: temp.append(' M |')
        else: temp.append('   |')
    print(''.join(temp))


for _ in range(int(input())):
    n,m=map(int,input().split())
    horizon='+'+('---+')*m
    board=[list(input()) for i in range(n)]
    visited=[[0]*m for i in range(n)]
    sol()
    print(f'Case: {_+1}')
    
    print(horizon)
    for i in range(n):
        printResult(i)
        print(horizon)
    if visited[-1][-1]: print('Minions can cross the room ')
    else: print('Minions cannot cross the room ')
    
