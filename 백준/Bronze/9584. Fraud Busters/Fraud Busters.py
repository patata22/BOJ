target=input()
answer=[]
for _ in range(int(input())):
    temp=input()
    same=True
    for i in range(len(target)):
        if target[i]=='*':continue
        if target[i]!=temp[i]:same=False
    if same:answer.append(temp)
print(len(answer))
print(*answer,sep='\n')
