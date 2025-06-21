n,m=map(int,input().split())
number=[0]+list(map(int,input().split()))
total=sum(number)
if total<m: print(-1)
else:
    for i in range(1,n+1):
        total-=number[i]
        if total<m:
            print(i)
            break

