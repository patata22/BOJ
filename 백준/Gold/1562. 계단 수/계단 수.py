DIV=10**9

n=int(input())

dp=[[[0]*1024 for i in range(10)] for i in range(n)]

for i in range(1,10):
    dp[0][i][1<<i]=1

for i in range(1,n):
    for x in range(10):
        for y in (-1,1):
            nx = x+y
            if 0<=nx<10:
                for j in range(1024):
                    dp[i][x][j|(1<<x)]+=dp[i-1][nx][j]
                dp[i][x][j|(1<<x)]%=DIV
answer=0
for i in range(10):
    answer+=dp[-1][i][1023]
print(answer%DIV)
