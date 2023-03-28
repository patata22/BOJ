def makeKey(word):
    if len(word)>1:
        return word[0]+''.join(sorted(list(word[1:len(word)-1])))+word[-1]
    else: return word

record={}
for _ in range(int(input())):
    key= makeKey(input())
    if key in record: record[key]+=1
    else: record[key]=1

for _ in range(int(input())):
    temp=1
    for x in input().split():
        if makeKey(x) in record:temp*=record[makeKey(x)]
        else:
            temp=0
            break
    print(temp)
