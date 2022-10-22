import sys
input=sys.stdin.readline

#J=0 O=1 I=2

n,m=map(int,input().split())
board = [[0]*(m+1)]
K=int(input())
for _ in range(n):
    board.append([0]+list(input().rstrip()))
dp= [[[0]*3 for i in range(m+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        for k in range(3):
            dp[i][j][k]=dp[i-1][j][k]+dp[i][j-1][k]-dp[i-1][j-1][k]
        if board[i][j]=='J':dp[i][j][0]+=1
        elif board[i][j]=='O':dp[i][j][1]+=1
        else: dp[i][j][2]+=1

for _ in range(K):
    a,b,c,d=map(int,input().split())
    for k in range(3):
        print(dp[c][d][k]-dp[a-1][d][k]-dp[c][b-1][k]+dp[a-1][b-1][k],end=' ')
    print()
