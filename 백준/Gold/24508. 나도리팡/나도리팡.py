from collections import deque

n,k,t=map(int,input().split())
number=sorted(list(map(int,input().split())))
total=0
l=0
r=n-1
if sum(number)%k!=0: print('NO')
else:
    while l<r:
        gap=k-number[r]
        if gap>number[l]:
            number[r]+=number[l]
            total+=number[l]
            l+=1
        elif gap==number[l]:
            total+=number[l]
            r-=1
            l+=1
    
        elif gap<number[l]:
            total+=gap
            number[l]-=gap
            r-=1

    print('YES') if total<=t else print('NO')
        
