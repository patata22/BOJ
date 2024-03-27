def getDistance(x,y,nx,ny):
    return abs(x-nx)+abs(y-ny)

def sol(x,y,hp,um,dist):
        ed = getDistance(x,y,ex,ey)
        if hp+um>=ed:
            global answer
            answer=min(answer,dist+ed)
            return
        for i in range(K):
            if used[i]:continue
            nx,ny=umbrella[i]
            D = getDistance(x,y,nx,ny)
            
            if hp+um>=D:
                used[i]=1
                if um>=D:sol(nx,ny,hp,d-1,dist+D)
                else:sol(nx,ny,hp-D+um+1,d-1,dist+D)
                used[i]=0
                    

n,h,d=map(int,input().split())
umbrella=[]
answer=float('inf')
for i in range(n):
    temp=list(input())
    for j in range(n):
        if temp[j]=='S': sx,sy=i,j
        elif temp[j]=='E': ex,ey=i,j
        elif temp[j]=='U': umbrella.append((i,j))
K=len(umbrella)
used=[0]*K
sol(sx,sy,h,0,0)
if answer==float('inf'):print(-1)
else:print(answer)
