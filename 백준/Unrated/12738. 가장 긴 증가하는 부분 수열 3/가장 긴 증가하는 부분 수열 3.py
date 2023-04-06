import bisect

n=int(input())
number=tuple(map(int,input().split()))
dp=[number[0]]

for x in number:
    if x>dp[-1]: dp.append(x)
    else:
        dp[bisect.bisect_left(dp,x)]=x
print(len(dp))
