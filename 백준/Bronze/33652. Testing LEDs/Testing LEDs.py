import sys
input=sys.stdin.readline

number=[]
for _ in range(int(input())):
    a,b=map(int,input().split())
    if not b: number.append(a)
if not number:print(-1)
else: print(sorted(number)[0])
