answer='TAK'
count={}
input()
for x in input().split():
    if x not in count:count[x]=1
    else: count[x]+=1
for i in range(1,5):
    for j in ('A','B','C'):
        if str(i)+j not in count:answer='NIE'
for j in ('5A','5B','5C'):
    if j not in count or count[j]<2:
        answer='NIE'
print(answer)