import sys
input=sys.stdin.readline

n=int(input())
table=[list(map(int,input().split())) for i in range(n)]
dp=[[0]*n for i in range(6)]
for i in range(n):
    a,b=table[i]
    dp[a][i]=dp[a][i-1]+1
    dp[b][i]=dp[b][i-1]+1

total=0
answer=0
for i in range(1,6):
    count=max(dp[i])
    if count>total:
        total=count
        answer=i
print(total,answer)
   