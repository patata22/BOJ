import sys
input=sys.stdin.readline

for tt in range(int(input())):
    n,k=map(int,input().split())
    number=sorted(list(map(int,input().split())))
    l=0
    r=n-1
    total=abs(k-number[0]-number[-1])
    count=0
    while l<r:
        temp = number[l]+number[r]
        gap=abs(k-temp)
        if gap<total:
            total=gap
            count=1

        elif gap==total:
            count+=1
        if temp<=k:
            l+=1
        else: r-=1
    print(count)
