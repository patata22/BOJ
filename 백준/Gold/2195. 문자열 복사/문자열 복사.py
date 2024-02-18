record=set()

word=input()
n=len(word)
for i in range(n):
    for j in range(i,n):
        temp=word[i:j+1]
        record.add(temp)

target=input()
idx=0
n=len(target)
temp=''
answer=0
while idx<n:
    if temp+target[idx] in record:
        temp+=target[idx]
    else:
        temp=target[idx]
        answer+=1
    idx+=1
if temp: answer+=1
print(answer)
