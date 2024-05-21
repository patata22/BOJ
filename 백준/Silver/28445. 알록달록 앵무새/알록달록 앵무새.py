body=input().split()
tail=input().split()
answer=set()

for x in body:
    for y in tail:
        answer.add((x,y))
for x in body:
    for y in body:
        answer.add((x,y))
for x in tail:
    for y in body:
        answer.add((x,y))
for x in tail:
    for y in tail:
        answer.add((x,y))
    
answer=sorted(list(answer))
for x in answer:print(*x)

