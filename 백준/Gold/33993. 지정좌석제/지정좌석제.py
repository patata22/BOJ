import sys
input=sys.stdin.readline

def check(x,y):
    for i in range(max(x-w,0),min(x+w+1,n)):
        for j in range(max(y-w,0),min(y+w+1,m)):
            board[i][j]+=1

N,n,m,w=map(int,input().split())
w//=2

board=[[0]*m for i in range(n)]

for _ in range(N):
    a,b=map(int,input().split())
    a-=1
    b-=1
    check(a,b)
    board[a][b]=-float('inf')

x,y=0,0
answer=-float('inf')

for i in range(n):
    for j in range(m):
        if board[i][j]>answer:
            x,y=i,j
            answer=board[i][j]

print(answer)
print(x+1,y+1)
        

