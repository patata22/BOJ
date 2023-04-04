def sol(x,depth):
    t=3**(depth-1)
    l=t
    r=2*t
    for i in range(x+l,x+r):answer[i]=' '
    if depth==1: return
    sol(x,depth-1)
    sol(x+r,depth-1)
        
while True:
    try:
        n=int(input())
        if not n:print('-')
        else:
            answer=['-']*(3**n)
            sol(0,n)
            print(*answer,sep='')
    except: break
