def sol(depth):
    global answer,h, w, e, o, l, r, d
    if answer: return
    if depth==7:
        if 10000*(w+h)+1001*o + 120*l + 1000*e + 100*r + d==n:
            answer=[[h,e,l,l,o],[w,o,r,l,d]]
            return
    if depth==0:
        for i in range(1,10):
            if not used[i]:
                used[i]=1
                h=i
                sol(depth+1)
                used[i]=0
    elif depth==1:
        for i in range(1,10):
            if not used[i]:
                used[i]=1
                w=i
                sol(depth+1)
                used[i]=0
    elif depth==2:
        for i in range(10):
            if not used[i]:
                used[i]=1
                e=i
                sol(depth+1)
                used[i]=0
    elif depth==3:
        for i in range(10):
            if not used[i]:
                used[i]=1
                o=i
                sol(depth+1)
                used[i]=0
    elif depth==4:
        for i in range(10):
            if not used[i]:
                used[i]=1
                l=i
                sol(depth+1)
                used[i]=0
    elif depth==5:
        for i in range(10):
            if not used[i]:
                used[i]=1
                r=i
                sol(depth+1)
                used[i]=0
    elif depth==6:
        for i in range(10):
            if not used[i]:
                used[i]=1
                d=i
                sol(depth+1)
                used[i]=0

n=int(input())
answer=[]
used=[0]*10
sol(0)
if not answer:print('No Answer')
else:
    print('  '+''.join(map(str,answer[0])))
    print('+ '+''.join(map(str,answer[1])))
    print('-------')
    if n>=100000:print(' '+str(n))
    else: print('  '+str(n))
