answer=0
price=0
number=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    number.append((a,b))

number.sort(key=lambda x: x[0], reverse=True)

while number:
    P,cost = number.pop()
    temp=P-cost
    for x,y in number:
        if P-y>=0:temp+=P-y
    if temp>answer:
        price=P
        answer=temp

print(price)
