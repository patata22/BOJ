n,k=map(int,input().split())
number = list(map(int,input().split()))
using=[]
answer=0
m=0
while len(using)<n:
    if number[m] not in using: using.append(number[m])
    m+=1
for i in range(m,k):
    now = number[i]
    if now in using: continue
    target=-1
    idx=-1
    for x in using:
        try:
            temp_idx = number[i+1:].index(x)
        except ValueError: temp_idx=float('inf')
        if temp_idx>idx:
            idx=temp_idx
            target=x
    using.remove(target)
    using.append(now)
    answer+=1
print(answer)
        
    
    
    
