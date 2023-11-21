for _ in range(int(input())):
    n=int(input())
    print(f'Case #{_+1}:', end=' ')
    if n==1:
        input()
        print(0)
    else:
        a,b=map(int,input().split())
        c,d=map(int,input().split())
        if (a<c and b>d) or (a>c and b<d):print(1)
        else:print(0)
