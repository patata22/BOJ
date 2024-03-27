n,k=map(int,input().split())

number=list(map(int,input().split()))
answer=0
now=20
for i in range(21):
    key=1<<(now-i)
    nxt=[]
    for x in number:
        if x&key: nxt.append(x)
    if len(nxt)>=k:
        answer+=key
        number=nxt
    else:
        continue
print(answer)
