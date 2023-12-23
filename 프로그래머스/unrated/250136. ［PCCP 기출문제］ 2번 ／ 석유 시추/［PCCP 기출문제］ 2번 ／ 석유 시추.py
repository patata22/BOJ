from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(board):
    n=len(board)
    m=len(board[0])
    answer=[0]*m
    visited=[[0]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:   
                count=1
                Y=set()
                q=deque()
                q.append((i,j))
                Y.add(j)
                visited[i][j]=1
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<m and board[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny]=1
                            q.append((nx,ny))
                            Y.add(ny)
                            count+=1
                for y in Y: answer[y]+=count
            
    return max(answer)