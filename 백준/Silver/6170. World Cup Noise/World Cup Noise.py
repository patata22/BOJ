import sys
input=sys.stdin.readline

for tt in range(int(input())):
    if tt:print()
    print(f'Scenario #{tt+1}:')
    n=int(input())
    dp=[[0]*2 for i in range(n)]
    dp[0][0]=1
    dp[0][1]=1
    for i in range(1,n):
        dp[i][0]+=sum(dp[i-1])
        dp[i][1]+=dp[i-1][0]
    print(sum(dp[-1]))
    