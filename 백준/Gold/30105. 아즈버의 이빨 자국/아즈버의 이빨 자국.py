def check(x):
    for i in number:
        if not (i-x in temp or i+x in temp): return False
    return True

n=int(input())
number=tuple(map(int,input().split()))
gap=set()
temp=set(number)
for i in range(1,n):
    gap.add(number[i]-number[0])
        

answer=[]
for x in gap:
    if check(x): answer.append(x)
print(len(answer))
answer.sort()
if answer:print(*answer)
