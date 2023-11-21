n=int(input())
board=[list(input()) for i in range(n)]
answer=[]
best=0
for j in range(5):
    count=0
    for i in range(n):
        if board[i][j]=='Y':
            count+=1
    if count>best:
        best=count
        answer=[j+1]
    elif count==best:
        answer.append(j+1)

print(*answer,sep=',')
