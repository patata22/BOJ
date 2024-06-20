n,m,c=map(int,input().split())
number=list(map(int,input().split()))
temp=[]
for i in range(c):
    cnt=number[i]
    for _ in range(cnt): temp.append(i+1)
number=temp
board=[[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        board[i][j]=number[i*m+j]


for i in range(1,n,2): board[i]=board[i][::-1]
for i in range(n):print(*board[i],sep='')
