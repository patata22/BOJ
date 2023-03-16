dx=(-1,-1,-1,0,0,0,1,1,1)
dy=(-1,0,1,-1,0,1,-1,0,1)

def solution(board):
    n=len(board)
    safe=[[1]*n for i in range(n)]
    answer = n*n
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for k in range(9):
                    nx,ny=i+dx[k], j+dy[k]
                    if 0<=nx<n and 0<=ny<n and safe[nx][ny]:
                        safe[nx][ny]=0
                        answer-=1
    return answer