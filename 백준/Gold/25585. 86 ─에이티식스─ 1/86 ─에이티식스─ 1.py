def sol(now, dist, killCount):
    global answer
    if killCount==unused:
        answer=min(answer,dist)
        return
    for to,d in distance[now]:
        if not destroyed[to]:
            destroyed[to]=1
            sol(to,dist+d,killCount+1)
            destroyed[to]=0

n=int(input())
unused=0
location={}
for i in range(n):
    temp=list(map(int,input().split()))
    for j in range(n):
        if 0<temp[j]<3:
            location[(i,j)]=unused
            if temp[j]==2: S=unused
            unused+=1

distance=[[] for i in range(unused)]
impossible=False
for x1,y1 in location:
    start=location[(x1,y1)]
    for x2,y2 in location:
        if x1==x2 and y1==y2:continue
        if (x1+y1)%2 != (x2+y2)%2: impossible=True
        to=location[(x2,y2)]
        gapX= abs(x1-x2)
        gapY= abs(y1-y2)
        gap=min(gapX,gapY)
        dist= gapX+gapY-gap
        distance[start].append((to,dist))

if impossible:print('Shorei')
else:
    destroyed=[0]*unused
    destroyed[S]=1
    answer=float('inf')
    sol(S,0,1)
    print('Undertaker')
    print(answer)
