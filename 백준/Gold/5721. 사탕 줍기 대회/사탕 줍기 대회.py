import sys
input=sys.stdin.readline

def sol(lst):
    N=len(lst)
    dp=[[0]*2 for i in range(N)]
    dp[0][1]=lst[0]
    for i in range(1,N):
        dp[i][0]=max(dp[i-1])
        dp[i][1]=dp[i-1][0]+lst[i]
    return max(dp[-1])
    

while True:
    n,m=map(int,input().split())
    if n==0: break
    print(sol([sol(list(map(int,input().split()))) for i in range(n)]))