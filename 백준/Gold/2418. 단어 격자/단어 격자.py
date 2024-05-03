dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)

n,m,l=map(int,input().split())

board=[list(input()) for i in range(n)]
dp=[[[0]*l for i in range(m)] for i in range(n)]

word=list(input())

s=word[0]
for i in range(n):
    for j in range(m):
        if board[i][j]==s:
            dp[i][j][0]=1

for k in range(1,l):
    s=word[k]
    b=word[k-1]
    for i in range(n):
        for j in range(m):
            if board[i][j]==s:
                for d in range(8):
                    nx,ny=i+dx[d],j+dy[d]
                    if 0<=nx<n and 0<=ny<m and board[nx][ny]==b:
                    
                        dp[i][j][k]+=dp[nx][ny][k-1]

answer=0
for i in range(n):
    for j in range(m):
        answer+=dp[i][j][-1]
print(answer)