import sys
input=sys.stdin.readline

n,m,q=map(int,input().split())

board=[[0]*m for i in range(n)]
row=[0]*n
col=[0]*m
for _ in range(q):
    c,x,v = map(int,input().split())
    if c==1: row[x-1]+=v
    else: col[x-1]+=v

for i in range(n):
    for j in range(m):
        board[i][j]=row[i]+col[j]

for i in range(n):
    print(*board[i])
    
