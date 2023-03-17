from collections import deque

dx=(-1,1,0,0)
dy=(0,0,-1,1)

def solution(maps):
    answer = []
    n=len(maps)
    m=len(maps[0])
    
    visited= [[0]*m for i in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X' and not visited[i][j]:
                visited[i][j]=1
                q=deque()
                q.append((i,j))
                temp = int(maps[i][j])
                while q:
                    x,y=q.popleft()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<n and 0<=ny<m and maps[nx][ny]!='X' and not visited[nx][ny]:
                            visited[nx][ny]=1
                            temp+=int(maps[nx][ny])
                            q.append((nx,ny))
                answer.append(temp)
    if not answer: return [-1]
    else: answer.sort()
    return answer