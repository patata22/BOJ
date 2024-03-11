DIV=10000

n,k=map(int,input().split())

dp=[[[0]*3 for i in range(3)] for i in range(n+1)]
select=[-1]*(n+1)
for _ in range(k):
    a,b=map(int,input().split())
    select[a]=b-1

a,b=select[1],select[2]
if a>=0 and b>=0:
    dp[2][a][b]=1
elif a>=0:
    for i in range(3):
        dp[2][a][i]=1
elif b>=0:
    for i in range(3):
        dp[2][i][b]=1
else:
    for i in range(3):
        for j in range(3):
            dp[2][i][j]=1

for i in range(3,n+1):
    a=select[i]
    if a>=0:
        if a==0:
            dp[i][0][0]=(dp[i-1][1][0]+dp[i-1][2][0])%DIV
            dp[i][1][0]=(dp[i-1][0][1]+dp[i-1][1][1]+dp[i-1][2][1])%DIV
            dp[i][2][0]=(dp[i-1][0][2]+dp[i-1][1][2]+dp[i-1][2][2])%DIV
        elif a==1:
            
            dp[i][0][1]=(dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])%DIV
            dp[i][1][1]=(dp[i-1][0][1]+dp[i-1][2][1])%DIV
            dp[i][2][1]=(dp[i-1][0][2]+dp[i-1][1][2]+dp[i-1][2][2])%DIV
        elif a==2:
            dp[i][0][2]=(dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])%DIV
            dp[i][1][2]=(dp[i-1][0][1]+dp[i-1][1][1]+dp[i-1][2][1])%DIV
            dp[i][2][2]=(dp[i-1][0][2]+dp[i-1][1][2])%DIV
    else:
        dp[i][0][0]=(dp[i-1][1][0]+dp[i-1][2][0])%DIV
        dp[i][1][0]=(dp[i-1][0][1]+dp[i-1][1][1]+dp[i-1][2][1])%DIV
        dp[i][2][0]=(dp[i-1][0][2]+dp[i-1][1][2]+dp[i-1][2][2])%DIV
        dp[i][0][1]=(dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])%DIV
        dp[i][1][1]=(dp[i-1][0][1]+dp[i-1][2][1])%DIV
        dp[i][2][1]=(dp[i-1][0][2]+dp[i-1][1][2]+dp[i-1][2][2])%DIV
        dp[i][0][2]=(dp[i-1][0][0]+dp[i-1][1][0]+dp[i-1][2][0])%DIV
        dp[i][1][2]=(dp[i-1][0][1]+dp[i-1][1][1]+dp[i-1][2][1])%DIV
        dp[i][2][2]=(dp[i-1][0][2]+dp[i-1][1][2])%DIV
        
answer=0
for i in range(3):
    for j in range(3):
        answer+=dp[-1][i][j]
print(answer%DIV)