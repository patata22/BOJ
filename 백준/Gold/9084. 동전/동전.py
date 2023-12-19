for _ in range(int(input())):
    n=int(input())
    coin=list(map(int,input().split()))
    goal=int(input())
    dp=[0]*(goal+1)
    dp[0]=1
    for i in coin:
        for j in range(1,goal+1):
            if j>=i:
                dp[j]+=dp[j-i]
    print(dp[-1])

