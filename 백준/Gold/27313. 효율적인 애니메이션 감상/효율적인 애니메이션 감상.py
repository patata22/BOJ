def sol():
    l=0
    r=n+1
    while l+1<r:
        mid=(l+r)//2
        target=[number[i] for i in range(mid)]
        time=0
        while target:
            time+=target[-1]
            for _ in range(k):
                if not target:break
                target.pop()
        if time>m: r=mid
        else: l=mid
        
    return l
                
n,m,k=map(int,input().split())
number=sorted(list(map(int,input().split())))
print(sol())