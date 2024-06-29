def sol():
    l=1
    r=n
    while(l+1<r):
        mid=(l+r)//2
        print('?', mid, flush=True)
        count=int(input())
        if count*2==mid:
            print('!', mid)
            return
        elif count*2>mid:
            l=mid
        else: r=mid
        
         
n=int(input())
sol()
