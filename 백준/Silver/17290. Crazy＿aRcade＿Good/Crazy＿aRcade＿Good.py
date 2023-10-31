x,y=map(int,input().split())
x-=1
y-=1

board=[]
row=[0]*10
col=[0]*10
for i in range(10):
    temp=input()
    for j in range(10):
        if temp[j]=='o':
            row[i]=1
            col[j]=1
    board.append(temp)
    
answer=float('inf')
for i in range(10):
    if row[i]: continue
    for j in range(10):
        if not col[j]:
            answer=min(answer,abs(x-i)+abs(j-y))
print(answer)
