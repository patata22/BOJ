n=int(input())
number=tuple(map(int,input().split()))
now=0
answer=0
for i in range(n):
    answer+=abs(now)
    now+=number[i]
print(answer)
