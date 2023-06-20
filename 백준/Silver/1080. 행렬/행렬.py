def reverse(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            board[i][j]=1-board[i][j]

n,m=map(int,input().split())
board=[list(map(int,list(input()))) for i in range(n)]
board2=[list(map(int,list(input()))) for i in range(n)]
answer=0
for i in range(n-2):
    for j in range(m-2):
        if board[i][j]!=board2[i][j]:
            reverse(i,j)
            answer+=1

flag=True
for i in range(n):
    for j in range(m):
        if board[i][j]!=board2[i][j]:
            flag=False
            break

if flag:print(answer)
else: print(-1)
