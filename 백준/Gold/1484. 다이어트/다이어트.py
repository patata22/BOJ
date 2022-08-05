answer=[]

l=1
r=1
R=51000
n=int(input())
while l<R and r<R:
    temp = r**2-l**2
    if temp==n:
        answer.append(r)
        l+=1
        r+=1
    if temp>n:
        l+=1
    elif temp<n:
        r+=1
if not answer:print(-1)
else:print(*answer,sep="\n")
