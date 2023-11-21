golden=1.61803399
l=golden*0.99
r=golden*1.01

for _ in range(int(input())):
    a,b=map(float,input().split())
    if l<=a/b<=r: print('golden')
    else:print('not')
