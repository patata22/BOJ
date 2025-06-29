import sys
input=sys.stdin.readline

def sol():
    a,b,c=input().split()
    a=list(a)
    b=list(b)
    c=list(c)
    A=len(a)+1
    B=len(b)+1
    dp=[[0]*B for i in range(A)]
    dp[0][0]=1
    for i in range(1,A):
        if a[i-1]==c[i-1] and dp[i-1][0]: dp[i][0]=1
    for i in range(1,B):
        if b[i-1]==c[i-1] and dp[0][i-1]: dp[0][i]=1
    for i in range(1,A):
        for j in range(1,B):
            now=c[i+j-1]
            
            if a[i-1]==now: dp[i][j]|=dp[i-1][j]
            if b[j-1]==now: dp[i][j]|=dp[i][j-1]
    if dp[-1][-1]:return'yes'
    else: return 'no'

for tt in range(1,int(input())+1):
    print(f'Data set {tt}: {sol()}')