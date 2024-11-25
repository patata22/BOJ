n,m=map(int,input().split())

number=list(map(int,input().split()))
number.sort()
n=sum(number)
total=0
count=0
while total*2<n:
    total+=number.pop()
    count+=1

print(m//(count+1))
