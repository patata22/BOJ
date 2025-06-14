answer=[0]*3
size=[0]*3
for i in range(3):
    a,b=map(int,input().split())
    size[i]=a
    answer[i]=b

now=0
for _ in range(100):
    nxt = (now+1)%3
    able=size[nxt]-answer[nxt]
    temp=min(able,answer[now])
    answer[now]-=temp
    answer[nxt]+=temp
    now=nxt
print(*answer,sep='\n')
