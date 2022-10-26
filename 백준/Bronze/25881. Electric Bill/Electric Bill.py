a,b=map(int,input().split())
for _ in range(int(input())):
    x=int(input())
    print(x,end=' ')
    if x>1000:
        print((x-1000)*b+1000*a)
    else: print(a*x)
    
