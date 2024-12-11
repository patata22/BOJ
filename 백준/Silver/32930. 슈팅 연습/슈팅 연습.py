n,m=map(int,input().split())
point=[tuple(map(int,input().split())) for i in range(n)]
answer=0
x,y=0,0
for _ in range(m):
    point.sort(key=lambda z: (x-z[0])**2+(y-z[1])**2)
    nx,ny=point.pop()
    answer+=(nx-x)**2+(ny-y)**2
    x,y=nx,ny
    point.append(tuple(map(int,input().split())))
    
print(answer)
