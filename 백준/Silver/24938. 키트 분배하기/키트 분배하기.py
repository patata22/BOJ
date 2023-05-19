n=int(input())
number=tuple(map(int,input().split()))
target=sum(number)//n
answer=0
gap=0
for x in number:
    gap+=(target-x)
    answer+=gap

print(answer)
