n,q=map(int,input().split())
number=tuple(map(int,input().split()))
prefix=[0]*n
for i in range(1,n):
    prefix[i]+=prefix[i-1]
    prefix[i]+=abs(number[i]-number[i-1])

for _ in range(q):
    a,b=map(int,input().split())
    print(prefix[b-1]-prefix[a-1])
