import sys
input=sys.stdin.readline

d,c,r=map(int,input().split())
answer=r
work=[int(input()) for i in range(c)]
for _ in range(r):
    d+=int(input())

for x in work:
    if d>=x:
        d-=x
        answer+=1
    else: break
print(answer)