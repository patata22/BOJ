import sys
input=sys.stdin.readline

n,m,q=map(int,input().split())
board=[list(map(int,input().split())) for i in range(n)]

for _ in range(q):
    temp = list(map(int,input().split()))
    if temp[0]:
        a,b,c = temp
        board[b],board[c]=board[c],board[b]
    else:
        a,b,c,d=temp
        board[b][c]=d

for i in range(n):
    print(*board[i])
