dx=(-1,0,1,0)
dy=(0,-1,0,1)
trans={'U':0, 'L':1, 'D':2, 'R':3}

def solution(dirs):
    answer=0
    x,y=5,5
    visited=[[[0]*4 for i in range(11)] for i in range(11)]
    for dir in dirs:
        dir=trans[dir]
        nx,ny = x+dx[dir], y+dy[dir]
        if 0<=nx<11 and 0<=ny<11:
            if not visited[x][y][dir]:
                visited[x][y][dir]=1
                visited[nx][ny][(dir+2)%4]=1
                answer+=1
            
            x,y=nx,ny
        
    return answer