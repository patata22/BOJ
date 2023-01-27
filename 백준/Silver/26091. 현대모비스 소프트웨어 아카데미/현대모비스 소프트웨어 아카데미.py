n,m=map(int,input().split())
number=sorted(list(map(int,input().split())))

l=0
r=n-1
answer=0
while l<r:
    if number[l]+number[r]>=m:
        answer+=1
        l+=1
        r-=1
    else:
        l+=1

print(answer)