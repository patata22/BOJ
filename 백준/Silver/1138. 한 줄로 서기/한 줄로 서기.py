n=int(input())
number=list(map(int,input().split()))
answer=[0]*n

for i in range(1,n+1):
    x=number[i-1]
    now=0
    count=0
    while count<x:
        if not answer[now]:
            count+=1
        now+=1
    while answer[now]:now+=1
    answer[now]=i
print(*answer)