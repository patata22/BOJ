n,m,k=map(int,input().split())
answer=0
l=0
r=0
left=[int(input()) for i in range(n)]
right=[int(input()) for i in range(m)]
quan=min(sum(left),sum(right))
while l<n and r<m:
    temp=min(left[l],right[r])

    answer+=temp*(l+r+2)
    left[l]-=temp
    if not left[l]:l+=1
    right[r]-=temp
    if not right[r]:r+=1
print(quan,answer)
