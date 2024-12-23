n,m=map(int,input().split())
count={}
for _ in range(n):
    input()
    for x in map(int,input().split()):
        if x not in count: count[x]=0
        count[x]+=1

answer=0
for x in count:
    if count[x]>=m: answer+=1
print(answer)
