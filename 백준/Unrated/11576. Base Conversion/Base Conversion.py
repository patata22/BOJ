a,b=map(int,input().split())
num=0
mul=1
m=input()
number=list(map(int,input().split()))[::-1]
for x in number:
    num+=mul*x
    mul*=a

answer=[]
while num:
    answer.append(num%b)
    num//=b

print(*answer[::-1])
