n,k=map(int,input().split())
number=tuple(map(int,input().split()))

answer=-1
l=0
r=0
count={number[0]:1}
while r<n-1:
    r+=1
    now=number[r]
    if now not in count: count[now]=1
    else:count[now]+=1
    while count[now]>k:
        left=number[l]
        count[left]-=1
        l+=1
    answer=max(answer,r-l+1)
print(answer)
            
            
