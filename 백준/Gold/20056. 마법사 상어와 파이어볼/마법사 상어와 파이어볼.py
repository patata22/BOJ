dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]

def moveAndSpread():
    
    mass_temp = [[0]*r for i in range(r)]
    speed_temp = [[0]*r for i in range(r)]
    count= [[0]*r for i in range(r)]
    direction= [[[] for i in range(r)] for i in range(r)]

    for _ in range(len(fireball)):
        x,y,m,s,d = fireball.pop()
        nx,ny = (x+s*dx[d])%r, (y+s*dy[d])%r
        mass_temp[nx][ny]+=m
        speed_temp[nx][ny]+=s
        count[nx][ny]+=1
        direction[nx][ny].append(d)
    
    for i in range(r):
        for j in range(r):
            if count[i][j] == 1:
                fireball.append((i,j,mass_temp[i][j],speed_temp[i][j], direction[i][j][0]))
            elif count[i][j]>1:
                nm = mass_temp[i][j]//5
                ns = speed_temp[i][j]//count[i][j]
                if nm:
                    odd=False
                    even=False
                    for d in direction[i][j]:
                        if d%2==0: even=True
                        if d%2==1: odd=True
                    if odd and even:
                        for d in range(1,8,2):
                            fireball.append((i,j , nm, ns, d))
                    else:
                        for d in range(0,8,2):
                            fireball.append((i,j,nm,ns,d))
                        
r,c,k = map(int,input().split())

fireball = []
for _ in range(c):
    x,y,m,s,d = map(int,input().split())
    x-=1
    y-=1
    fireball.append((x,y,m,s,d))

for _ in range(k):
    moveAndSpread()

answer=0
for x in fireball:
    answer+=x[2]
print(answer)
