import sys
input=sys.stdin.readline

lines=sorted(list(tuple(map(int,input().split())) for i in range(int(input()))), reverse=True)
answer=0

a,b=lines.pop()
l=a
r=b

while lines:
    a,b=lines.pop()
    if a>r:
        answer+=(r-l)
        l,r=a,b
    else:
        r=max(r,b)
answer+=r-l

print(answer)

