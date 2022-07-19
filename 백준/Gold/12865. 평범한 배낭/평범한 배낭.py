n,k=map(int,input().split())
item = [list(map(int,input().split())) for i in range(n)]
dp=[[0]*(k+1) for i in range(n)]

for i in range(n):
    for w in range(k+1):
        w_i, v_i = item[i]
        if w_i>w: dp[i][w]=dp[i-1][w]
        else: dp[i][w]= max(v_i + dp[i-1][w-w_i], dp[i-1][w])
print(dp[-1][-1])
