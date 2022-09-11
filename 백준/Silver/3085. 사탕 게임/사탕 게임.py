def check_row(x):
    global answer
    now=board[x][0]
    long=1
    streak=1
    for i in range(1,n):
        if board[x][i]==board[x][i-1]:
            streak+=1
        else:
            long=max(long,streak)
            now=board[x][i]
            streak=1
    long=max(streak,long)
    answer=max(answer,long)
    return long

def check_col(x):
    global answer
    now=board[0][x]
    long=1
    streak=1
    for i in range(1,n):
        if board[i][x]==now:
            streak+=1
        else:
            long=max(long,streak)
            now=board[i][x]
            streak=1
    long=max(streak,long)
    answer=max(answer,long)
    return long

def sol():
    for i in range(n):
        for j in range(n):
            if i!=n-1:
                board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
                check_row(i)
                check_row(i+1)
                check_col(j)
                board[i][j],board[i+1][j]=board[i+1][j],board[i][j]
            if j!=n-1:
                board[i][j+1],board[i][j]=board[i][j],board[i][j+1]
                check_col(j)
                check_col(j+1)
                check_col(i)
                
                board[i][j+1],board[i][j]=board[i][j],board[i][j+1]

n=int(input())
board=[list(input()) for i in range(n)]
answer=0
for i in range(n):
    check_row(i)
    check_col(i)

sol()
print(answer)
