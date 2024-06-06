n=int(input())
number=list(map(int,input().split()))
total=[0]
for i in range(n):
    total.append(total[-1]+number[i])

answer=[]
answer.append(number[0])
gap=number[0]
for i in range(1,n):
    gap+=total[i]*2+number[i]
    temp = answer[-1]+gap
    answer.append(temp)

print(*answer)
