import sys
input=sys.stdin.readline

s,n,m=map(int,input().split())
size=0
for _ in range(n+m):
    if int(input()):
        size+=1
        if size>s: s*=2
    else: size-=1
print(s)
