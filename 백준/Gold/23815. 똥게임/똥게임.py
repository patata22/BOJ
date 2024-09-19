import sys
input=sys.stdin.readline


n=int(input())
cmd=[[]]
for _ in range(n):
    cmd.append(input().split())

dp=[[-float('inf')]*2 for i in range(n+1)]
dp[0][0]=1

for i in range(1,n+1):
    dp[i][1]=dp[i-1][0]
    for c in cmd[i]:
        x=int(c[1])
        if c[0]=='+':
            dp[i][0]=max(dp[i][0],dp[i-1][0]+x)
            dp[i][1]=max(dp[i][1],dp[i-1][1]+x)
        elif c[0]=='-':
            if dp[i-1][0]-x>0:
                dp[i][0]=max(dp[i][0],dp[i-1][0]-x)
            if dp[i-1][1]-x>0:
                dp[i][1]=max(dp[i][1],dp[i-1][1]-x)
        elif c[0]=='*':
            dp[i][0]=max(dp[i][0],dp[i-1][0]*x)
            dp[i][1]=max(dp[i][1],dp[i-1][1]*x)
        else:
            if dp[i-1][0]//x:
                dp[i][0]=max(dp[i][0],dp[i-1][0]//x)
            if dp[i-1][1]//x:
                dp[i][1]=max(dp[i][1],dp[i-1][1]//x)
answer=max(dp[-1])
if answer==-float('inf'): print('ddong game')
else: print(answer)  