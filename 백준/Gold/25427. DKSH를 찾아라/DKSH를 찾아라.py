n=int(input())
word=input()
answer=0

DKSH={'D':0,'K':1,'S':2,'H':3}
dp=[[0]*4 for i in range(n)]

answer=0
for i in range(n):
    w=word[i]
    if w not in DKSH:
        for j in range(4):
            dp[i][j]=dp[i-1][j]
    elif w=='D':
        dp[i][0]=dp[i-1][0]+1
        for j in range(1,4):
            dp[i][j]=dp[i-1][j]
    else:
        for j in range(4):
            if DKSH[w]==j:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            else: dp[i][j]=dp[i-1][j]
print(dp[-1][-1])
        
                
                
