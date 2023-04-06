import bisect

for _ in range(int(input())):
    n,k=map(int,input().split())
    number=tuple(map(int,input().split()))
    dp=[number[0]]
    for x in number:
        if x>dp[-1]: dp.append(x)
        else: dp[bisect.bisect_left(dp,x)]=x
    print(f'Case #{_+1}\n{int(len(dp)>=k)}')
