n=int(input())
number=tuple(map(int,input().split()))

dp=[[0]*201 for i in range(101)] 
for x in number:
    for i in range(-100,101):
        before=x-i
        if 1<=before<=100:
            dp[x][i]=max(dp[x][i],dp[before][i]+1)
        else:
            dp[x][i]=max(dp[x][i],1)
answer=0
for i in range(101):
    for j in range(201):
        answer=max(answer,dp[i][j])
print(answer)
