dx=(-1,1,0,0,0,0)
dy=(0,0,-1,1,0,0)
dz=(0,0,0,0,-1,1)

cube=set()
n,m=map(int,input().split())
for _ in range(m):
    a,b,c=map(int,input().split())
    cube.add((a,b,c))
answer=0
for x,y,z in cube:
    count=0
    for i in range(6):
        nx,ny,nz=x+dx[i],y+dy[i],z+dz[i]
        if (nx,ny,nz) in cube: count+=1
    if count==6: answer+=1
print(answer)