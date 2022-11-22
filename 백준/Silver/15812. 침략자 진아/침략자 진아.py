def sol(a,b):
    global answer
    temp = 0
    x1,y1=a
    x2,y2=b

    for x,y in home:
        d = min(abs(x-x1)+abs(y-y1), abs(x-x2)+abs(y-y2))
        temp = max(temp,d)
    answer= min(temp, answer)
    

n,m=map(int,input().split())

space = []
home = []
board = []
for i in range(n):
    temp = tuple(map(int,list(input())))
    for j in range(m):
        if temp[j]==1: home.append((i,j))
        else: space.append((i,j))

answer = float('inf')
l = len(space)
for i in range(l):
    for j in range(i+1,l):
        sol(space[i], space[j])

print(answer)
