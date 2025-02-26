import sys,bisect
input=sys.stdin.readline

for tt in range(int(input())):
    number=[int(input()) for _ in range(int(input()))]
    dp=[number[0]]
    for x in number:
        if x>dp[-1]: dp.append(x)
        else:
            idx=bisect.bisect_left(dp,x)
            dp[idx]=x
    print(len(dp))
        
