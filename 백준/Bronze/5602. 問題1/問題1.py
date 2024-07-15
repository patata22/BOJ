n,m=map(int,input().split())
count=[0]*m
for _ in range(n):
    temp=list(map(int,input().split()))
    for j in range(m):
        count[j]+=temp[j]
answer=[i for i in range(1,m+1)]
answer.sort(key=lambda x: count[x-1], reverse=True)
print(*answer)
