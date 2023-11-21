n=int(input())
now=1
answer=0
number=list(map(int,input().split()))
for x in number:
    if x!=now: answer+=1
    else: now+=1
print(answer)
