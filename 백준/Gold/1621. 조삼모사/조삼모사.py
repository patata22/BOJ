n=int(input())
k,c=map(int,input().split())

number=[0]+list(map(int,input().split()))
track=[i-1 for i in range(n+1)]
cnt=[0]*(n+1)

dp=[float('inf')]*(n+1)
dp[0]=0

if k>n:
    print(sum(number))
    print(0)
    
else:
    for i in range(1,k):
        dp[i]=dp[i-1]+number[i]
    for i in range(k,n+1):
        one=dp[i-1]+number[i]
        jump=dp[i-k]+c
        if jump<one:
            dp[i]=jump
            track[i]=i-k
            cnt[i]=cnt[i-k]+1
        elif jump>one:
            dp[i]=one
            track[i]=i-1
            cnt[i]=cnt[i-1]
        else:
            if cnt[i-k]+1<cnt[i-1]:
                dp[i]=jump
                track[i]=i-k
                cnt[i]=cnt[i-k]+1
            else:
                dp[i]=one
                track[i]=i-1
                cnt[i]=cnt[i-1]
            
    print(dp[-1])
    history=[]
    now=n
    while now>0:
        prev=track[now]
        if cnt[now]>cnt[prev]: history.append(prev+1)
        now=prev
    print(len(history))
    print(*history[::-1])
    