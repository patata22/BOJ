import sys
input=sys.stdin.readline
n,c=map(int,input().split())
number=sorted(list(map(int,input().split())))
flag=0
r=set()
for x in number:
    if x==c: flag=1
    r.add(x)
for x in number:
    if c-x in r and x!=c-x: flag=1

for i in range(n):
    x=number[i]
    for j in range(i+1,n):
        y=number[j]
        temp=c-x-y
        if temp!=x and temp!=y and temp in r: flag=1
print(flag)