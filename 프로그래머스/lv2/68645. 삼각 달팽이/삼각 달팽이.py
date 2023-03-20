direction=((1,0), (0,1), (-1,-1))

def solution(n):
    board=[[0]*i for i in range(1,n+1)]
    
    x,y,d=0,0,0
    for i in range(1,(n*n+n)//2+1):
        board[x][y]=i
        nx,ny=x+direction[d][0], y+direction[d][1]
        if 0<=nx<n and 0<=ny<len(board[nx]) and not board[nx][ny]:
            x,y=nx,ny
        else:
            d=(d+1)%3
            x,y=x+direction[d][0], y+direction[d][1]
    answer=[]
    for i in range(n): answer+=board[i]
    return answer