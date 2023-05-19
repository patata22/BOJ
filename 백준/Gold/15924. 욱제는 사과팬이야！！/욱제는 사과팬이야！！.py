import sys
input=sys.stdin.readline

def sol():
    DIV=10**9+9
    n,m=map(int,input().split())
    dp=[[1]*(m+1) for i in range(n+1)]
    for i in range(n):
        temp=input()
        for j in range(m):
            x=dp[i][j]
            if temp[j]=='B':
                dp[i][j+1]=(x+dp[i][j+1])%DIV
                dp[i+1][j]=(x+dp[i+1][j])%DIV
            elif temp[j]=='S':
                dp[i+1][j]=(x+dp[i+1][j])%DIV
            else:
                dp[i][j+1]=(x+dp[i][j+1])%DIV
    return dp[-2][-2]

print(sol())
