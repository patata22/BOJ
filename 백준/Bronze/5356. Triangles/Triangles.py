nxt={}
for i in range(65,91):
    nxt[chr(i)]=chr(i+1)
nxt['Z']='A'

for _ in range(int(input())):
    if _:print()
    answer=[]
    n,now=input().split()
    for __ in range(int(n)):
        answer.append(now*(__+1))
        now=nxt[now]
    for x in answer:print(x)