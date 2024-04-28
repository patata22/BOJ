
target=[' ']+list(input())
m=len(target)
board=[[' ']+list(input()) for i in range(2)]
n=len(board[0])
dp=[[[0]*2 for i in range(m)] for i in range(n)]

dp[0][0][0]=1
dp[0][0][1]=1

for i in range(1,n):
    for j in range(m):
        t=target[j]
        for k in range(2):
            dp[i][j][k]+=dp[i-1][j][k]
            if board[k][i]==t:
                dp[i][j][k]+=dp[i-1][j-1][1-k]
print(sum(dp[-1][-1]))
