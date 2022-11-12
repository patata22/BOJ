for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if c*d>a*b: print('Eurecom')
    elif c*d==a*b: print('Tie')
    else:print('TelecomParisTech')
