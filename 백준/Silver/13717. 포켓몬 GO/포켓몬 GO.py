total=0
maxCount=0
maxName=""

for _ in range(int(input())):
    name=input()
    count=0
    a,b=map(int,input().split())
    while b>=a:
        count+=1
        b-=a-2
    if count>maxCount:
        maxCount=count
        maxName=name
    total+=count
print(total)
print(maxName)
