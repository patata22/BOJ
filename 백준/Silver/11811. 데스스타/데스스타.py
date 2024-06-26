n=int(input())

board=[list(map(int,input().split())) for i in range(n)]
answer=[]
for i in range(n):
    temp=0
    for j in range(n):
        temp|=board[i][j]
        temp|=board[j][i]
    answer.append(temp)

print(*answer)
