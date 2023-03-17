from collections import deque
dx=(1,0,-1,0)
dy=(0,1,0,-1)

def solution(places):
    answer = []
    for place in places:
        safe = 1
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P' and check(i,j,place):
                    safe=0
                    break
        print(safe)
        answer.append(safe)                    
    return answer

def check(a,b,board):
    q=deque()
    q.append((a,b))
    visited=[[0]*5 for i in range(5)]
    visited[0][0]=1
    t=0
    while q and t<2:
        for _ in range(len(q)):
            x,y=q.popleft()
            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]
                if 0<=nx<5 and 0<=ny<5 and board[nx][ny]!='X' and not visited[nx-a][ny-b]:
                    if board[nx][ny]=='P': return True
                    visited[nx-a][ny-b]=1
                    q.append((nx,ny))
        t+=1
    return False