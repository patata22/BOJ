def change(x):
    temp=x
    while len(temp)<10:
        temp+=x
    return int(temp[:10])

n,k=map(int,input().split())
number=sorted([input() for i in range(n)], key=lambda x: -change(x))
bonus=sorted(number, key=lambda x: (-len(x), -change(x)))[0]

answer=[]
flag=True
for x in number:
    if flag and x==bonus:
        flag=False
        for i in range(k-n+1):answer.append(x)
    else: answer.append(x)
print(''.join(answer))
