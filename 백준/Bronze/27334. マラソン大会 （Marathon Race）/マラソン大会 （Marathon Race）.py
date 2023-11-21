rank={}

n=int(input())
number=list(map(int,input().split()))
temp=sorted(number)
for i in range(n):
    if temp[i] not in rank: rank[temp[i]]=i+1
for x in number:print(rank[x])
