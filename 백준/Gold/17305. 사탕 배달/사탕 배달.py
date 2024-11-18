import sys
input=sys.stdin.readline

n,w=map(int,input().split())

three=[]
five=[]

for _ in range(n):
    a,b=map(int,input().split())
    if a==3: three.append(b)
    else: five.append(b)

three.sort()
five.sort()
answer=0

fivesack=[]

while five and w-5>=0:
    w-=5
    x=five.pop()
    answer+=x
    fivesack.append(x)

while three and w-3>=0:
    w-=3
    answer+=three.pop()

temp=answer
while three and fivesack:
    temp-=fivesack.pop()
    w+=5
    while three and w-3>=0:
        w-=3
        temp+=three.pop()
    answer=max(answer,temp)

print(answer)

