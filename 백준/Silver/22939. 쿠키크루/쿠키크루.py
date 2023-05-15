def sol(x,y,count,location,d,name):
    global answer,dist

    if count==3:
        if d+abs(x-ex)+abs(y-ey)<dist:
            dist=d+abs(x-ex)+abs(y-ey)
            answer=name
        return
    for i in range(3):
        if not used[i]:
            used[i]=1
            nx,ny=location[i]
            sol(nx,ny,count+1, location, d+abs(nx-x)+abs(ny-y), name)
            used[i]=0

n=int(input())
J=[]
C=[]
B=[]
W=[]
used=[0]*3
for i in range(n):
    x=list(input())
    for j in range(n):
        if x[j]=='H':sx,sy=i,j
        elif x[j]=='J': J.append((i,j))
        elif x[j]=='C': C.append((i,j))
        elif x[j]=='B': B.append((i,j))
        elif x[j]=='W': W.append((i,j))
        elif x[j]=='#': ex,ey=i,j

dist=float('inf')
answer=""

sol(sx,sy,0,J,0,'Assassin')
sol(sx,sy,0,C,0,'Healer')
sol(sx,sy,0,B,0,'Mage')
sol(sx,sy,0,W,0,'Tanker')

print(answer)
