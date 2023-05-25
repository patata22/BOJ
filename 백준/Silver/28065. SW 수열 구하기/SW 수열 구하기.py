answer=[]
l=1
r=int(input())
t=0
while l<=r:
    t+=1
    if t%2:
        answer.append(l)
        l+=1
    else:
        answer.append(r)
        r-=1
print(*answer)
