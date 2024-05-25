a,b=map(int,input().split())
if a not in (0,2,5) and b not in (0,2,5):print('=')
elif a not in (0,2,5):
    print('<')
elif b not in (0,2,5):
    print('>')
elif a==b: print('=')
else:
    if a==0:
        if b==2: print('>')
        elif b==5: print('<')
    elif a==2:
        if b==5: print('>')
        elif b==0: print('<')
    elif a==5:
        if b==0: print('>')
        elif b==2:print('<')
