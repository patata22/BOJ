def solution(m, n, puddles):
    DIV=1000000007
    dp=[[0]*m for i in range(n)]
    puddle=set()
    for y,x in puddles:
        puddle.add((x-1,y-1))
    dp[0][0]=1
    for x in range(n):
        for y in range(m):
            if (x,y) not in puddle:
                for dx,dy in ((-1,0), (0,-1)):
                    nx,ny=x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m:
                        dp[x][y]+=dp[nx][ny]
            dp[x][y]%=DIV

    return dp[-1][-1]
