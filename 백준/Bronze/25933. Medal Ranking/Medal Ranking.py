for _ in range(int(input())):
    if _:print()
    a1,b1,c1,a2,b2,c2=map(int,input().split())
    print(a1,b1,c1,a2,b2,c2)
    count=True
    color=True
    if a2+b2+c2>=a1+b1+c1: count=False
    if (a1,b1,c1)<=(a2,b2,c2):color=False
    if count and color: print('both')
    elif count: print('count')
    elif color: print('color')
    else: print('none')
    
