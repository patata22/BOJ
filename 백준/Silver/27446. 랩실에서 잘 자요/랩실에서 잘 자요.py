n,m=map(int,input().split())
page=[0]*(n+1)
for i in set(map(int,input().split())):page[i]=1

now=0
jump=0
count=0
include=0
answer=0
while now<n:
    now+=1
    if page[now]:
        if not include: continue
        jump+=1
        if jump==3:
            answer+=2*(count-jump+1)+5
            jump=0
            count=0
            include=0
            continue
        count+=1
    else:
        include=1
        count+=1
        jump=0
if include: answer+=2*(count-jump)+5

print(answer)
