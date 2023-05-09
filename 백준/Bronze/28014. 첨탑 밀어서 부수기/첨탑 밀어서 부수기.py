n=int(input())
number=tuple(map(int,input().split()))
answer=0
now=0
for i in range(n):
    if now<=number[i]:
        answer+=1
    now=number[i]
print(answer)