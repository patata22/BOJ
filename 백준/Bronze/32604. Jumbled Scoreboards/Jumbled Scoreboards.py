def sol():
    x,y=0,0
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if not (a>=x and b>=y): return 'no'
        x,y=a,b
    return 'yes'

print(sol())
