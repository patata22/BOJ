from collections import deque

record={}
sentence=[]
for i in range(int(input())):
    temp=input().split()
    for x in temp: record[x]=i
    sentence.append(deque(temp))
answer='Possible'

for x in input().split():
    if x not in record:
        answer='Impossible'
        break
    num=record[x]
    if sentence[num][0]==x:
        sentence[num].popleft()
    else:
        answer='Impossible'
        break

for x in sentence:
    if x: answer='Impossible'
print(answer)
