import sys
input=sys.stdin.readline


DIV=10**9+7

dp=[0]*10000001
dp[1]=5
dp[2]=20

for i in range(3,10000001):
    dp[i]=(dp[i-1]*5)%DIV

for _ in range(int(input())):
    print(dp[int(input())])
