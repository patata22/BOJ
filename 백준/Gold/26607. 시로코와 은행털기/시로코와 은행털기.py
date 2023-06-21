n,K,x=map(int,input().split())
number=[]
for _ in range(n):
    a,b=map(int,input().split())
    number.append(a)

dp=[[[0]*(K*x+1) for i in range(K+1)] for i in range(n)]
for i in range(n):
    temp=number[i]
    dp[i][0][0]=1
    dp[i][1][temp]=1
    for j in range(1,K+1):
        for k in range(K*x+1):
            dp[i][j][k]|=dp[i-1][j][k]
            if k>=temp:dp[i][j][k]|=dp[i-1][j-1][k-temp]
    
total=K*x
answer=0
for i in range(1,total):
    if dp[-1][-1][i]:
        answer=max(answer,i*(total-i))
print(answer)