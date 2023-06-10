a=['one','two','three','four','five','six','seven','eight','nine']
b=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
d=[x+'hundred' for x in a]
value={}
record={}
count=0
temp=[0]

for x in a:
    record[x]=len(x)
    count+=1
    value[x]=count
    temp.append(x)
for x in b:
    record[x]=len(x)
    count+=1
    value[x]=count
    temp.append(x)
for x in c:
    record[x]=len(x)
    count+=1
    value[x]=count
    temp.append(x)
    for y in a:
        record[x+y]=len(x+y)
        count+=1
        value[x+y]=count
        temp.append(x+y)
for x in d: 
    record[x]=len(x)
    count+=1
    value[x]=count
    temp.append(x)
    for y in a:
        record[x+y]=len(x+y)
        count+=1
        value[x+y]=count
        temp.append(x+y)
    for y in b:
        record[x+y]=len(x+y)
        count+=1
        value[x+y]=count
        temp.append(x+y)
    for y in c:
        record[x+y]=len(x+y)
        count+=1
        value[x+y]=count
        temp.append(x+y)
        for z in a:
            record[x+y+z]=len(x+y+z)
            count+=1
            value[x+y+z]=count
            temp.append(x+y+z)

word=[]
total=0

for _ in range(int(input())):
    x=input()
    if x=='$': target=_
    else:
        total+=len(x)
    word.append(x)

for x in record:
    if total+record[x]==value[x]:
        word[target]=x
        break

print(' '.join(word))
