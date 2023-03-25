import sys
input=sys.stdin.readline

n,a=map(int,input().split())

board=[[float('inf')]*(n+1) for i in range(n+1)]

for _ in range(a):
    a,b=map(int,input().split())
    board[a][b]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if board[i][j]>board[i][k]+board[k][j]:
                board[i][j]=board[i][k]+board[k][j]

for _ in range(int(input())):
    a,b= map(int,input().split())
    if board[a][b]!=float('inf'): print(-1)
    elif board[b][a]!=float('inf'): print(1)
    else: print(0)