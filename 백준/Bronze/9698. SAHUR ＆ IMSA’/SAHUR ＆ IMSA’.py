for t in range(1,int(input())+1):
    h,m=map(int,input().split())
    total=60*h+m
    total=total-45
    total%=1440
    print(f'Case #{t}: {total//60} {total%60}')
    
