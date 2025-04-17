number=[]

while True:
    try:number.append(tuple(map(int,input().split())))
    except: break

n=len(number)
dp=[[[0]*16 for i in range(16)] for i in range(n)]
dp[0][1][0]=number[0][0]
dp[0][0][1]=number[0][1]

for i in range(1,n):
    w,b=number[i]
    for j in range(16):
        for k in range(16):
            dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k])
            if j>0: dp[i][j][k]=max(dp[i][j][k],dp[i-1][j-1][k]+w)
            if k>0: dp[i][j][k]=max(dp[i][j][k],dp[i-1][j][k-1]+b)

print(dp[-1][-1][-1])