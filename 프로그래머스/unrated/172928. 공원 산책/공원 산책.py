dx=(-1,0,1,0)
dy=(0,-1,0,1)

def solution(board, routes):
    directions={'N':0, 'S':2, 'W':1, 'E':3}
    n=len(board)
    m=len(board[0])
    for i in range(n):
        for j in range(m):
            if board[i][j]=='S': x,y = i,j
    
    def move(x, y, route):
        d,long = route.split()
        d=directions[d]
        long=int(long)
        nx,ny=x,y
        for i in range(long):
            nx,ny=nx+dx[d],ny+dy[d]
            if not (0<=nx<n and 0<=ny<m) or board[nx][ny]=='X': return x,y
        return nx,ny
    for route in routes:
        x,y= move(x,y,route)
    return x,y