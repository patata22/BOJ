for _ in range(int(input())):
    a,b,c=sorted(list(map(int,input().split())))
    d,e,f=sorted(list(map(int,input().split())))
    if c**2==a**2+b**2 and a==d and b==e and c==f: print('YES')
    else: print('NO')
