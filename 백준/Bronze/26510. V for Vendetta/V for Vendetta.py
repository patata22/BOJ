def sol(n,now):
    print(' '*(n-now), end='')
    if now==1:
        print('*')
        return
    print('*',end='')
    print(' '*(2*now-3),end='')
    print('*')
    sol(n,now-1)

for x in map(int,input().split()):
    sol(x,x)