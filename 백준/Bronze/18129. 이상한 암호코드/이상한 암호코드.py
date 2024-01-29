word,k=input().split()
word=list(word.lower())
k=int(k)
record=set()
n=len(word)
now=word[0]
count=1
answer=[]
for i in range(1,n):
    if word[i]==now: count+=1
    else:
        if word[i] in record:continue
        else:
            record.add(now)
            if count>=k:
                answer.append(1)
            else: answer.append(0)
            now=word[i]
            count=1
if now not in record:
    if count>=k:
        answer.append(1)
    else: answer.append(0)
print(*answer,sep='')
