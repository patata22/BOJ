import sys
input=sys.stdin.readline

n=int(input())
song=tuple(map(int,input().split()))
dp=[0]*n
for i in range(1,n):
    dp[i]=dp[i-1]
    if song[i]<song[i-1]:
        dp[i]+=1

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(dp[b-1]-dp[a-1])
