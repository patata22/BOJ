n=int(input())
number=list(map(int,input().split()))
answer=0
fruit=0
count={}
for x in number: count[x]=0
l=-1
r=0
while l+1<n:
    l+=1
    now=number[l]
    if count[now]==0:fruit+=1
    count[now]+=1
    while fruit>2:
        now=number[r]
        count[now]-=1
        if count[now]==0: fruit-=1
        r+=1
    answer=max(answer,l-r+1)
   
print(answer)