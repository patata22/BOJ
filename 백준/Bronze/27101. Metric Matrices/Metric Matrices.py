answer=float('inf')

n=int(input())
board=[list(map(int,input().split())) for i in range(n)]


for i in range(n):
    if board[i][i]!=0: answer=min(answer,1)
    for j in range(i+1,n):
        if board[i][j]<0:answer= min(answer,2)
        if board[i][j]!=board[j][i]:answer=min(answer,3)
for i in range(n):
    for j in range(n):
        for k in range(n):
            if board[i][j]+board[j][k]<board[i][k]: answer=min(answer,4)
if answer==float('inf'):answer=0
print(answer)
