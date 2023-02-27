input()
count={}
count[0]=0
for i in range(65):count[2**i]=0
for x in tuple(map(int,input().split())):
    count[x]+=1

now=1
for i in range(64):
    if count[now]:answer=now
    temp=count[now]
    now*=2
    count[now]+=temp//2
print(answer)