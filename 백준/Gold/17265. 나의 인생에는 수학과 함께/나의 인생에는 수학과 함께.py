dx=(1,0)
dy=(0,1)

def sol(x,y,lastNum, lastCal):
    if not x and not y:
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if nx<n and ny<n:
                sol(nx,ny,lastNum, lastCal)
        return
    if board[x][y].isdigit():
        if lastCal=='+':
            num = lastNum+int(board[x][y])
        elif lastCal=='-':
            num = lastNum-int(board[x][y])
        elif lastCal=='*':
            num = lastNum*int(board[x][y])
        if x==n-1 and y==n-1:
            global maxAnswer, minAnswer
            maxAnswer = max(maxAnswer, num)
            minAnswer = min(minAnswer, num)
            return
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if nx<n and ny<n:
                sol(nx,ny,num, lastCal)
        
    else:
        for i in range(2):
            nx,ny=x+dx[i],y+dy[i]
            if nx<n and ny<n:
                sol(nx,ny,lastNum, board[x][y])

n=int(input())
board=[list(input().split()) for i in range(n)]

maxAnswer=-float('inf')
minAnswer=float('inf')

sol(0,0,int(board[0][0]),'.')
print(maxAnswer, minAnswer)
