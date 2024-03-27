a,b,c,d=map(int,input().split())
if a==d and b==c:
    print('JAH')
    print(a,b,c,d)
elif a!=d and b!=c:
    print('EI')
elif a!=d:
    print('JAH')
    print(a,b,c,a)
else:
    print('JAH')
    print(a,b,b,d)
