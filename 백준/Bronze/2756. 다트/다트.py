for _ in range(int(input())):
    a=list(map(float, input().split()))
    s1,s2=0,0
    for i in range(0,6,2):
        x=a[i]
        y=a[i+1]
        d=x**2+y**2
        if d<=9: s1+=100
        elif d<=36: s1+=80
        elif d<=81:s1+=60
        elif d<=144:s1+=40
        elif d<=225: s1+=20
    for i in range(6,12,2):
        x=a[i]
        y=a[i+1]
        d=x**2+y**2
        if d<=9: s2+=100
        elif d<=36: s2+=80
        elif d<=81:s2+=60
        elif d<=144:s2+=40
        elif d<=225: s2+=20
    
    print(f'SCORE: {s1} to {s2},',end=' ')
    if s1>s2:print('PLAYER 1 WINS.')
    elif s1<s2:print('PLAYER 2 WINS.')
    else:print('TIE.')