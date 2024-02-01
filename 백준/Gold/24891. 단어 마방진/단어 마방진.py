def sol(depth):
    global answer
    if answer: return
    if depth==l:
        for i in range(l):
            for j in range(l):
                if board[i][j]!=board[j][i]:
                    return
        answer=1
        return
    for i in range(n):
        if not used[i]:
            used[i]=1
            board.append(word[i])
            sol(depth+1)
            if answer:return
            board.pop()
            used[i]=0

l,n=map(int,input().split())

word=sorted([input() for i in range(n)])
answer=0
used=[0]*n
board=[]
sol(0)
if answer:
    print(*board, sep='\n')
else: print('NONE')