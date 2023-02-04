n=int(input())
board=[list(input()) for i in range(n)]

now=0
answer="YES"
while now<n:
    for i in range(now,n):
        if board[now][i]!=board[i][now]:answer="NO"
    now+=1
    if answer=="NO": break
print(answer)
