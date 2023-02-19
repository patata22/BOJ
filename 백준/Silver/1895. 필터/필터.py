def sol(i,j):
    temp=[]
    for x in range(i,i+3):
        for y in range(j,j+3):
            temp.append(board[x][y])
    return sorted(temp)[4]
    

n,m=map(int,input().split())

board=[tuple(map(int,input().split())) for i in range(n)]

f=[]

for i in range(n-2):
    for j in range(m-2):
        f.append(sol(i,j))

answer=0
t=int(input())
for x in f:
    if x>=t:answer+=1

print(answer)

