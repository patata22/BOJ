n,k=map(int,input().split())

number=[0]+list(map(int,input().split()))

total=[0]*(n+1)

for i in range(1,n+1):
    total[i]=total[i-1]
    if number[i]==1: total[i]+=1
answer=float('inf')
l=1
r=1
while r<=n:
   count=total[r]-total[l-1]
   if count>=k:
       answer=min(answer, r-l+1)
       l+=1
   else: r+=1

print(-1) if answer==float('inf') else print(answer) 

        
