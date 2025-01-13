import sys
input=sys.stdin.readline


def checkR(x):
    dp=[[0]*2 for i in range(n)]
    for y in range(n):
        if board[x][y]==1:
            dp[y][0]=max(dp[y][0],dp[y-1][0]+1)
            dp[y][1]=max(dp[y][1],dp[y-1][1]+1)
        elif board[x][y]==2:
            dp[y][1]=max(dp[y][1],dp[y-1][0]+1)
    result=0
    for i in range(n):
        result=max(result,max(dp[i]))
    return result

def checkC(y):
    dp=[[0]*2 for i in range(n)]
    for x in range(n):
        if board[x][y]==1:
            dp[x][0]=max(dp[x][0],dp[x-1][0]+1)
            dp[x][1]=max(dp[x][1],dp[x-1][1]+1)
        elif board[x][y]==2:
            dp[x][1]=max(dp[x][1],dp[x-1][0]+1)
    result=0
    for i in range(n):
        result=max(result,max(dp[i]))
    return result

def checkRD(x,y):
    dp=[[0]*2 for i in range(n)]
    temp=0
    while x<n and y<n:
        if board[x][y]==1:
            dp[temp][0]=max(dp[temp][0],dp[temp-1][0]+1)
            dp[temp][1]=max(dp[temp][1],dp[temp-1][1]+1)
        elif board[x][y]==2:
            dp[temp][1]=max(dp[temp][1],dp[temp-1][0]+1)
        temp+=1
        x+=1
        y+=1
    result=0
    for i in range(temp):
        result=max(result,max(dp[i]))
    return result

def checkLD(x,y):
    dp=[[0]*2 for i in range(n)]
    temp=0
    while x>=0 and y<n:
        if board[x][y]==1:
            dp[temp][0]=max(dp[temp][0],dp[temp-1][0]+1)
            dp[temp][1]=max(dp[temp][1],dp[temp-1][1]+1)
        elif board[x][y]==2:
            dp[temp][1]=max(dp[temp][1],dp[temp-1][0]+1)
        temp+=1
        x-=1
        y+=1
    result=0
    for i in range(temp):
        result=max(result,max(dp[i]))
    return result

n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
answer=0
for x in range(n):
    answer=max(answer,checkR(x),checkC(x),checkRD(0,x),checkRD(x,0), checkLD(n-1,x),checkLD(x,0))

print(answer)
