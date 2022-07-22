DIV=1234567
near={1:(2,4), 2:(1,3,5), 3:(2,6), 4:(1,5,7),5:(2,4,6,8),6:(3,5,9),7:(4,8,0),8:(5,7,9),9:(6,8),0:[7]}
for _ in range(int(input())):
    n=int(input())
    dp=[[0]*10 for i in range(n+1)]
    for i in range(10):
        dp[1][i]=1
    for i in range(2,n+1):
        for j in range(10):
            temp=near[j]

            for x in temp:
                
                dp[i][j]+=dp[i-1][x]
            dp[i][j]%=DIV
    print(sum(dp[n])%1234567)
      
