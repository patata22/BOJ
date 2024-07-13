def calc(x):
    head=temp
    tail=1
    cnt=1
    result={x:temp}
    while cnt<temp:
        head*=temp-cnt
        cnt+=1
        if x*cnt>m: break
        tail*=cnt
        result[x*cnt]=head//tail
    return result

n,m=map(int,input().split())
count=list(map(int,input().split()))
record={0:1}
count[0]=0
answer=[]
for i in range(1,m+1):
    if not count[i]:continue
    temp=count[i]
    for _ in range(temp): answer.append(i)
    re=calc(i)
    ad={}
    for x in record:
        for y in re:
            if x+y>m: continue
            if x+y in ad: ad[x+y]+=record[x]*re[y]
            else: ad[x+y]=record[x]*re[y]
            count[x+y]-=record[x]*re[y]
    for x in ad:
        if x in record: record[x]+=ad[x]
        else: record[x]=ad[x]
print(*answer)