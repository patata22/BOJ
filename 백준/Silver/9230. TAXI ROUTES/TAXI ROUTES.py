import sys
input=sys.stdin.readline

t=0
while True:
    t+=1
    n,m=map(int,input().split())
    if not n: break
    board=[[0]*m for i in range(n)]
    while True:
        a,b=map(int,input().split())
        if not a and not b: break
        board[a][b]=1

    dp=[[0]*m for i in range(n)]
    dp[0][0]=1
    for i in range(n):
        for j in range(m):
            if board[i][j]: continue
            if j-1>=0: dp[i][j]+=dp[i][j-1]
            if i-1>=0: dp[i][j]+=dp[i-1][j]

    print(f'Map {t}: {dp[-1][-1]}')
            