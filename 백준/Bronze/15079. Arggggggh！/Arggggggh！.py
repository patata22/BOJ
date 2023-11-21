r2=2**0.5

n=int(input())
x,y=map(int,input().split())
for _ in range(n-1):
    cmd, d = input().split()
    d=int(d)
    if len(cmd)==2: d/=r2
    if 'N' in cmd: y+=d
    if 'S' in cmd: y-=d
    if 'W' in cmd: x-=d
    if 'E' in cmd: x+=d
print(x,y)
    
