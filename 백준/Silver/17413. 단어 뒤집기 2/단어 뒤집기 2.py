word=list(input())
temp=[]
answer=[]
reverse=True
now=-1
n=len(word)
while now+1<n:
    now+=1
    if word[now]=='<':
        reverse=False
        while temp: answer.append(temp.pop())
        answer.append(word[now])
        
        continue
    elif word[now]=='>':
        reverse=True
        answer.append(word[now])
        continue
    elif word[now]==' ':
        
        if reverse:
            while temp: answer.append(temp.pop())
        answer.append(' ')
        continue
    if not reverse:
        answer.append(word[now])
    else:
        temp.append(word[now])
while temp: answer.append(temp.pop())

print(''.join(answer))
        
    
        
