n=int(input())
number=list(map(int,input().split()))
total=sum(number)
for x in number:
    if 2*x!=total:print(x,end=' ')
print(total//2)
