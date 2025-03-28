import sys
input=sys.stdin.readline

for tt in range(int(input())):
    n,m=map(int,input().split())
    left=0
    right=0
    board=[tuple(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(m):
            if (i+j)%2: left+=board[i][j]
            else: right+=board[i][j]
    if left==right:print('YES')
    else: print('NO')