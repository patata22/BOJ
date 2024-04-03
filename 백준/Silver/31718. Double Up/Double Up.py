def parse(x):
    x=int(x)
    while not x%2:
        x//=2
    return x

n=int(input())
number=list(map(parse,input().split()))

count={}
for x in number:
    if x not in count:count[x]=0
    count[x]+=1

answer=0
for x in count:answer=max(answer,count[x])
print(answer)
    
