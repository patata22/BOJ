n,m=map(int,input().split())
board=[list(input()) for i in range(n)]

answer=[]

for i in range(n):
    temp=[]
    for j in range(m):
        if board[i][j]=='#':
            if len(temp)>1:
                answer.append(''.join(temp))
            temp=[]
        else: temp.append(board[i][j])
    if len(temp)>1: answer.append(''.join(temp))

for i in range(m):
    temp=[]
    for j in range(n):
        if board[j][i]=='#':
            if len(temp)>1:
                answer.append(''.join(temp))
            temp=[]
        else: temp.append(board[j][i])
    if len(temp)>1: answer.append(''.join(temp))
answer.sort()
print(answer[0])
