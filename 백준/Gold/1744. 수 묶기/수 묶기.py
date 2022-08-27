pos=[]
neg=[]
zero=False
answer=0
for _ in range(int(input())):
    n=int(input())
    if n>1:pos.append(n)
    elif n==1: answer+=1
    elif n==0: zero=True
    else: neg.append(n)

pos.sort()
neg.sort(reverse=True)


while pos:
    try:
        a=pos.pop()
        b=pos.pop()
        answer+=a*b
    except:
        answer+=a

while neg:
    try:
        a=neg.pop()
        b=neg.pop()
        answer+=a*b
    except:
        if not zero: answer+=a

print(answer)
