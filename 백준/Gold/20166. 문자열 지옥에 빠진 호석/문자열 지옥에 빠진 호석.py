dx=(-1,-1,-1,0,0,1,1,1)
dy=(-1,0,1,-1,1,-1,0,1)


def sol(x,y,word):
    temp=word+board[x][y]
    
    if temp in count: count[temp]+=1
    if len(temp)>4: return
    for i in range(8):
        nx,ny=(x+dx[i])%n, (y+dy[i])%m
        sol(nx,ny,temp)

n,m,k=map(int,input().split())
board=[list(input()) for i in range(n)]
word=[input() for i in range(k)]
count={}
for x in word:
    count[x]=0

for i in range(n):
    for j in range(m):
        sol(i,j,"")

for x in word:
    print(count[x])
