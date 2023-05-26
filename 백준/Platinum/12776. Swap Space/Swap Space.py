import sys
input=sys.stdin.readline

answer=0
space=0

pos=[]
neg=[]

for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<b: pos.append((a,b))
    else: neg.append((a,b))
pos.sort(key=lambda x: x[0])
neg.sort(key=lambda x: -x[1])

for a,b in pos:
    space-=a
    if space<0: answer=min(answer,space)
    space+=b

for a,b in neg:
    space-=a
    if space<0: answer=min(answer,space)
    space+=b
print(-answer)

