count={}
input()
for x in input():
    if x in "' ,":continue
    if x not in count: count[x]=1
    else: count[x]+=1

answer=0
for x in count: answer=max(answer,count[x])
print(answer)
