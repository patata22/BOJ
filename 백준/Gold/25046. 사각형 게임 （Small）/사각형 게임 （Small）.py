def woo(depth):
    if depth==n:
        global answer
        answer=max(answer,jong())
        return
    woo(depth+1)
    row[depth]=1
    woo(depth+1)
    row[depth]=0

def jong():
    temp=0
    for j in range(n):
        total=0
        A=[0,0]
        for i in range(n):
            A[row[i]]+=board[i][j]
            total+=board[i][j]
        temp+=total-max(A)
    return temp


n=int(input())
board=[list(map(int,input().split())) for i in range(n)]
row=[0]*n
answer=-float('inf')
woo(0)
print(answer)
