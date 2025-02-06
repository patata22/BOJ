import sys
input=sys.stdin.readline

n=int(input())

number=[list(map(int,input().split())) for i in range(n)]

dp=[[0]*2 for i in range(n)]

dp[0][0]=number[0][0]
dp[0][1]=number[0][1]

for i in range(1,n):
   dp[i][0]=number[i][0]+max(dp[i-1][0]+abs(number[i-1][1]-number[i][1]),dp[i-1][1]+abs(number[i-1][0]-number[i][1]))
   dp[i][1]=number[i][1]+max(dp[i-1][0]+abs(number[i-1][1]-number[i][0]),dp[i-1][1]+abs(number[i-1][0]-number[i][0]))

print(max(dp[-1]))               

