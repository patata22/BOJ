num={'H':1, 'C':12, 'O':16}

chem= list(input())

answer=[0]
multi=[]

while chem:
    x=chem.pop()
    if 49<ord(x)<58:
        multi.append(int(x))
        y=chem.pop()
        if y==')':
            answer.append(0)
        else: answer[-1]+=num[y]*multi.pop()
    elif x==')':
        multi.append(1)
        answer.append(0)

    elif x=='(':
        a=answer.pop()
        answer[-1]+=a*multi.pop()
    else: answer[-1]+=num[x]
print(answer[0])