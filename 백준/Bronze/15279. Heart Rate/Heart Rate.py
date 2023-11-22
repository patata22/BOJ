for _ in range(int(input())):
    b,p=input().split()
    p=float(p)
    b=int(b)
    x=b/p
    y=(b+1)/p
    print(60*(b-1)/p,60*b/p,60*(b+1)/p)