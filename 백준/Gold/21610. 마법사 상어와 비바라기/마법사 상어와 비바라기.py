from collections import deque

dx = (0, 0,-1,-1,-1,0,1,1,1)
dy = (0,-1,-1, 0,  1,1,1,0,-1)

def rain(d,s):
    visited= [[0]*n for i in range(n)]
    for _ in range(len(cloud)):
        x,y = cloud.popleft()
        nx, ny = (x+s*dx[d])%n, (y+s*dy[d])%n
        visited[nx][ny] = 1
        board[nx][ny]+=1
    for x in range(n):
        for y in range(n):
            if visited[x][y]:
                temp = 0
                for i in range(2,9,2):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]:
                        temp+=1
                board[x][y]+=temp

    for x in range(n):
        for y in range(n):
            if not visited[x][y] and board[x][y]>1:
                board[x][y]-=2
                cloud.append((x,y))
                

    
    

n,m=map(int,input().split())

board = [list(map(int,input().split())) for i in range(n)]

cloud=  deque([(n-1,0), (n-1,1), (n-2,0), (n-2,1)])

for _ in range(m):
    rain(*map(int,input().split()))

answer=0
for i in range(n):
    answer+=sum(board[i])

print(answer)

