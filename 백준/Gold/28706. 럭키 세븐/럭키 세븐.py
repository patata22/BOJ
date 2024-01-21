import sys
input=sys.stdin.readline

for _ in range(int(input())):

    n=int(input())
    dp=[[0]*7 for i in range(n+1)]
    dp[0][1]=1
    for t in range(n):
        a,b,c,d=input().rstrip().split()
        b,d=int(b),int(d)
        if a=='+':
            for i in range(7):
                if dp[t][i]:
                    dp[t+1][(i+b)%7]=1
        else:
            for i in range(7):
                if dp[t][i]:
                    dp[t+1][(i*b)%7]=1
        if c=='+':
            for i in range(7):
                if dp[t][i]:
                    dp[t+1][(i+d)%7]=1
        else:
            for i in range(7):
                if dp[t][i]:
                    dp[t+1][(i*d)%7]=1
    if dp[-1][0]:print('LUCKY')
    else:print('UNLUCKY')
