import sys
input=sys.stdin.readline

for _ in range(int(input())):
    n=int(input())
    board=[list(map(int,input().split())) for i in range(2)]
    a,b,c,d=map(lambda x: int(x)-1,input().split())
    if a>c: a,b,c,d=c,d,a,b
    if a==c:
        left=board[b][a]+board[1-b][a]
        right=board[d][c]+board[1-d][c]
    else:
        left=max(board[b][a],board[b][a]+board[1-b][a])
        right=max(board[d][c],board[d][c]+board[1-d][c])
    for i in range(a-1,-1,-1):
        board[0][i]+=board[0][i+1]
        board[1][i]+=board[1][i+1]
        left=max(board[1][i]+board[0][i+1],board[0][i]+board[1][i+1], board[0][i]+board[1][i],left)
    for i in range(c+1,n):
        board[0][i]+=board[0][i-1]
        board[1][i]+=board[1][i-1]
        right=max(board[1][i]+board[0][i-1],board[0][i]+board[1][i-1],board[0][i]+board[1][i],right)
    middle=0    
    for i in range(a+1,c):
        middle+=max(board[0][i],board[1][i],board[0][i]+board[1][i])
    if a==c:
        print(max(left,right,board[b][a]+board[d][c]))
    else:
        print(middle+left+right)
