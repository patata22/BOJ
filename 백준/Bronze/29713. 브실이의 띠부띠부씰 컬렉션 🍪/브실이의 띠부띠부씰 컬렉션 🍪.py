target='BRONZESILVER'
count={}
for x in target: count[x]=0

input()
for x in input():
    if x in count:
        count[x]+=1
answer=10**6
for x in target:
    if x in ('R', 'E'): answer=min(count[x]//2, answer)
    else:   answer=min(count[x],answer)
print(answer)
