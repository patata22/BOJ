import sys
input=sys.stdin.readline

board=[]
original=list('SciComLove')
n,q=map(int,input().split())
for i in range(n):
    if original[i%10].isupper():board.append(1)
    else:board.append(0)

answer=sum(board)
for _ in range(q):
    x=int(input())-1
    if board[x]: answer-=1
    else: answer+=1
    board[x]=1-board[x]
    print(answer)