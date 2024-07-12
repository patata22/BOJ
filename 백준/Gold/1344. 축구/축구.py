

dp=[[[0]*2 for i in range(19)] for i in range(19)]
dp[0][0][0]=1
dp[0][0][1]=1

a,b=int(input()),int(input())

#i=시간
#j=점수
for i in range(1,19):
    for j in range(19):
        if j!=0:
            dp[i][j][0]+=dp[i-1][j-1][0]*a
            dp[i][j][1]+=dp[i-1][j-1][1]*b

        dp[i][j][0]+=dp[i-1][j][0]*(100-a)
        dp[i][j][1]+=dp[i-1][j][1]*(100-b)

prime=[2,3,5,7,11,13,17]
answer=0
for p in prime:
    answer+=dp[-1][p][0]
    answer+=dp[-1][p][1]

for x in prime:
    for y in prime:
        answer-=(dp[-1][x][0]*dp[-1][y][1])/(10**36)
        
            


print(answer/(10**36))
