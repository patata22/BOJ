def flip(x,y):
    for i in range(x,-1,-1):
        for j in range(y,-1,-1):
            board[i][j]=1-board[i][j]

n,m=map(int,input().split())

board=[list(map(int,list(input()))) for i in range(n)]
answer=0

for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if board[i][j]:
            flip(i,j)
            answer+=1

print(answer)