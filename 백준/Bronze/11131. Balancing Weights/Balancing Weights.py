for _ in range(int(input())):
    input()
    x=sum(map(int,input().split()))
    if x>0:print('Right')
    elif x<0:print('Left')
    else:print('Equilibrium')