n=int(input())
number=tuple(map(int,input().split()))
arrow=[0]*(1000001)
for x in number:
    if arrow[x]:
        arrow[x]-=1
        arrow[x-1]+=1
    else: arrow[x-1]+=1
print(sum(arrow))