for _ in range(int(input())):
    n=int(input())
    l=1
    r=n
    while l+1<r:
        mid = (l+r)//2
        if mid*(mid+1)>2*n: r = mid
        else: l = mid
    print(l)
    
    
