input()
answer=0
number=tuple(map(int,input().split()))
temp=set(number)
for x in temp:
    answer=max(answer,number.count(x))
print(answer)
