n=int(input())
number=list(map(lambda x: int(x)-1, input().split()))

answer=0
for i in range(n):
    if number[i]==i:
        number[i] = (i+1)%n
        answer+=1
for i in range(n):
    number[i]+=1
print(answer)
print(*number)
