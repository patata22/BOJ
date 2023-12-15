c,r=map(int,input().split())
x,y=0,0
while True:
    a,b=map(int,input().split())
    if not a and not b:
        break
    x+=a
    y+=b
    x=max(0,x)
    x=min(c,x)
    y=max(0,y)
    y=min(r,y)
    print(x,y)
    
