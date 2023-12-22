import sys
input=sys.stdin.readline

n=int(input())
task=[tuple(map(int,input().split())) for i in range(n)]
dp=[[0]*2 for i in range(n)]

for i in range(n):
    dp[i][0]=max(dp[i-1])
    dp[i][1]=dp[i-1][0]+task[i][2]
print(max(dp[-1]))