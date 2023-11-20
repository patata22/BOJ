def row(i):
    now='.'
    count=0
    answer=[]
    for j in range(m):
        if now=='.':
            if board[i][j]=='#':
                count=1
        else:
            if board[i][j]=='#':
                count+=1
            else:
                answer.append(count)
                count=0
        now=board[i][j]
    if now=='#': answer.append(count)
    if not answer:answer.append(0)
    return answer

def col(j):
    now='.'
    count=0
    answer=[]
    for i in range(n):
        if now=='.':
            if board[i][j]=='#':
                count=1
        else:
            if board[i][j]=='#':
                count+=1
            else:
                answer.append(count)
                count=0
        now=board[i][j]
    if now=='#': answer.append(count)
    if not answer:answer.append(0)
    return answer

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
for i in range(n):print(*row(i))
for i in range(m):print(*col(i))