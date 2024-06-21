n,q=map(int,input().split())
number=list(map(int,input().split()))
mul=[]
for i in range(n):
    mul.append(number[i]*number[(i+1)%n]*number[(i+2)%n]*number[(i+3)%n])
answer=sum(mul)
uk=list(map(lambda x: int(x)-1,input().split()))
for x in uk:
    for i in range(4):
        target=mul[(x-i)%n]
        answer-=2*target
        mul[(x-i)%n]*=-1
    print(answer)
