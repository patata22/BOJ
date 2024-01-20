n=int(input())
answer=0
for x in input().split():
    temp=str(x)
    if temp==temp[::-1]:answer+=int(temp)
print(answer)
