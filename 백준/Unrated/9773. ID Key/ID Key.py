for _ in range(int(input())):
    x=list(input())
    a=sum(map(int,x))
    b=int(''.join(x))%1000*10
    c=a+b
    if c<1000: c+=1000
    else: c%=10000
    c=str(c)
    print((4-len(c))*'0'+c)
    