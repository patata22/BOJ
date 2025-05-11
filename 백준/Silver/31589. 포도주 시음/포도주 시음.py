n,k=map(int,input().split())
l=0
r=n-1
number=sorted(map(int,input().split()))
answer=0
before=0
for i in range(k):
    if not i%2:
        answer+=number[r]-before
        r-=1
    else:
        before=number[l]
        l+=1
print(answer)
