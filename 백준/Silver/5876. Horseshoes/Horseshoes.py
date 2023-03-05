dx=(-1,1,0,0)
dy=(0,0,-1,1)


def sol(x,y,left,right,depth):
    global answer
    if left==right:answer=max(answer,left*2)
    for i in range(4):
        nx,ny=x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and (nx,ny) not in visited:
            if board[nx][ny]=='(' and not right:
                visited.add((nx,ny))
                sol(nx,ny,left+1,right,depth+1)
                visited.remove((nx,ny))
            elif board[nx][ny]==')' and right<left:
                visited.add((nx,ny))
                sol(nx,ny,left,right+1,depth+1)
                visited.remove((nx,ny))
        
            
    

n=int(input())
board = [tuple(input()) for i in range(n)]
visited=set()
answer=0

if board[0][0]==')':print(0)
else:
    visited.add((0,0))
    sol(0,0,1,0,1)
    print(answer)
