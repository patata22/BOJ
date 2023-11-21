n,r,c=map(int,input().split())

for _ in range(n):
    board=[list(input()) for i in range(r)]
    for i in range(r):
        if '#' in board[i]:
            up=i
            break
    for i in range(r-1,-1,-1):
        if '#' in board[i]:
            bottom=i
            break
    print(bottom-up)
    