def sol():
    x,y=map(int,input().split())
    z=2*(x+y)
    n=1
    while n*(n+1)<z:n+=1
    win=0
    while n:
        if n<=x:
            x-=n
            win+=1
        elif n<=y:
            y-=n
        else: return -1
        n-=1
    return win

print(sol())