import sys
input=sys.stdin.readline

n,m,q=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]

for i in range(1,n):
    for j in range(m):
        board[i][j]+=board[i-1][j]
for i in range(1,n):
    for j in range(1,m):
        board[i][j]+=board[i-1][j-1]

answer=[]
for _ in range(q):
    a,b=map(int,input().split())
    answer.append(board[a-1][b-1])
print(*answer, sep='\n')