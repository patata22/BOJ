import sys
input=sys.stdin.readline

DIV=1000000007

dp=[[0]*5 for i in range(1000001)]
dp[1][0]=1
dp[1][1]=1
dp[1][2]=1

for i in range(2,1000001):
    dp[i][0]=sum(dp[i-1])%DIV
    dp[i][1]=(dp[i-1][1]+dp[i-1][4])%DIV
    dp[i][2]=(dp[i-1][2]+dp[i-1][3])%DIV
    dp[i][3]=(dp[i-1][0]+dp[i-1][3])%DIV
    dp[i][4]=(dp[i-1][0]+dp[i-1][4])%DIV

for tt in range(int(input())):
    x=int(input())
    print((dp[x][0]+dp[x][3]+dp[x][4])%DIV)