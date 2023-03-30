import sys
input=sys.stdin.readline
n=int(input())
p={}
for _ in range(n-1):
    a,b=input().rstrip().split()
    p[a]=b

a,b=input().rstrip().split()
flag=False
if a not in p or b not in p: flag=True
now=a
while now in p:
    if now==b:
        flag=True
        break
    now = p[now]

now=b
while now in p:
    if now==a:
        flag=True
        break
    now = p[now]

if flag: print(1)
else: print(0)
