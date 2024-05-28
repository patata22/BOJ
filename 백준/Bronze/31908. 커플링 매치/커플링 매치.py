ring={}
for _ in range(int(input())):
    a,b=input().split()
    if b=='-': continue
    if b not in ring:
        ring[b]=[]
    ring[b].append(a)
answer=[]
for x in ring:
    if len(ring[x])==2: answer.append(ring[x])
print(len(answer))
for x in answer:
    print(*x)
    
