def reverseNum(n):
    temp=[]
    for x in n:
        temp.append(record[x])
    return ''.join(temp[::-1])

def change(x):
    temp=x
    while len(temp)<10:
        temp+=x
    return int(temp[:10])
    
record={'0':'0', '1':'1', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}

n=int(input())
number=list(map(lambda x: reverseNum(x), input().split()))
number.sort(key=lambda x: (len(x), change(x)))
last=number[-1]
number.sort(key=lambda x: -change(x))
flag=True
answer=[]
for x in number:
    if flag and x==last:
        flag=False
        answer.append(x)
    answer.append(x)
print(reverseNum(''.join(answer)))
                          