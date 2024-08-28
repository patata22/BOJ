import sys
input=sys.stdin.readline

def find(x,y):
    if p[x][y]==(-1,-1): return (x,y)
    p[x][y]=find(*p[x][y])
    return (p[x][y][0],p[x][y][1])

def union(x1,y1,x2,y2):
    a1,a2=find(x1,y1)
    b1,b2=find(x2,y2)
    if not (a1==b1 and a2==b2):
        p[b1][b2]=(a1,a2)

n,m=map(int,input().split())
board=[list(input()) for i in range(n)]
p=[[(-1,-1) for i in range(m)] for i in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j]=='U':
            union(i,j,i-1,j)
        elif board[i][j]=='D':
            union(i,j,i+1,j)
        elif board[i][j]=='R':
            union(i,j,i,j+1)
        else:
            union(i,j,i,j-1)

answer=0
for i in range(n):
    for j in range(m):
        if p[i][j][0]==-1: answer+=1
print(answer)