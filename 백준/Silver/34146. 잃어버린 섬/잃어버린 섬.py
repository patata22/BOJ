n,m=map(int,input().split())

count={}
for _ in range(n):
    for x in map(int,input().split()):
        if x not in count: count[x]=0
        count[x]+=1

answer='YES'
if m%2:
    temp=0
    for x in count:
        temp+=count[x]%2
        
    if temp>n: answer='NO'
else:
    for x in count:
        if count[x]%2: answer='NO'
print(answer)
    

