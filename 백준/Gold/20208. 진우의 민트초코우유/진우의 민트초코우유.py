def sol(x,y,energy,eat):
    
    global answer
    if abs(x-sx)+abs(y-sy)<=energy: answer=max(answer,eat)
    for i in range(l):
        if not visited[i]:
            x2,y2=choco[i]
            distance = abs(x-x2)+abs(y-y2)
            if distance<=energy:
                visited[i]=1
                sol(x2,y2,energy-distance+h, eat+1)
                visited[i]=0
            
n,m,h=map(int,input().split())
choco=[]
answer=0

for i in range(n):
    temp=tuple(map(int,input().split()))
    for j in range(n):
        if temp[j]==2: choco.append((i,j))
        elif temp[j]==1: sx,sy=i,j

l=len(choco)
visited=[0]*l

sol(sx,sy,m,0)

print(answer)
