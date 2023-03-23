dx=(-1,0,1,0)
dy=(0,-1,0,1)
#  좌= +1 우= -1


def solution(grid):
    answer = []
    n=len(grid)
    m=len(grid[0])
    visited= [[[0]*4 for i in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k]:
                    x,y,d = i,j,k
                    t=0
                    while not visited[x][y][d]:
                        visited[x][y][d]=1
                        t+=1
                        x,y=(x+dx[d])%n, (y+dy[d])%m
                        if grid[x][y]=='L': d=(d+1)%4
                        elif grid[x][y]=='R': d=(d-1)%4
                    answer.append(t)
    answer.sort()
    return answer