while True:
    n,k=map(int,input().split())
    if not n: break
    number=[-10001]+list(map(int,input().split()))
    dp=[[0]*(k+1) for i in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        now=number[i]
        for j in range(1,k+1):
            for l in range(i-1,-1,-1):
                if number[l]<=now:
                    dp[i][j]+=dp[l][j-1]
    answer=0
    for i in range(1,n+1):
        answer+=dp[i][-1]
    print(answer)
        