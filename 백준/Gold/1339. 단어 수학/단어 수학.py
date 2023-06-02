value={}
for _ in range(int(input())):
    x=list(input())
    i=1
    while x:
        now=x.pop()
        if now not in value:
            value[now]=i
        else: value[now]+=i
        i*=10
    
temp=[x for x in value]
temp.sort(key=lambda x: value[x], reverse=True)
number={}
now=9
for x in temp:
    number[x]=now
    now-=1
answer=0
for x in temp:
    answer+=number[x]*value[x]
print(answer)
