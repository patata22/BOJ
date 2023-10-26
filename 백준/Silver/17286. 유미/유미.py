def sol(depth, total,x,y):
    global answer
    if depth==3:
        answer=min(answer,int(total))
        return
    for i in range(3):
        if not used[i]:
            used[i]=1
            nx,ny=point[i]
            sol(depth+1, total+((nx-x)**2+(ny-y)**2)**0.5,nx,ny)
            used[i]=0
            
        

x,y=map(int,input().split())
point=[tuple(map(int,input().split())) for i in range(3)]
used=[0]*3
answer=float('inf')
sol(0,0,x,y)
print(answer)
