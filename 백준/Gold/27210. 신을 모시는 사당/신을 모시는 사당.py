n=int(input())

number=tuple(map(int,input().split()))
answer=0
l,r=0,0
for x in number:
    if x==1:
        l+=1
        r-=1
    else:
        l-=1
        r+=1

    if l<0:l=0
    if r<0:r=0

    answer=max(answer,l,r)
print(answer)
