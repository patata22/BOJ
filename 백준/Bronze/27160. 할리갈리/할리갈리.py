import sys
input=sys.stdin.readline

count={}
for _ in range(int(input())):
    a,b=input().split()
    b=int(b)
    if a not in count: count[a]=b
    else: count[a]+=b
answer='NO'
for x in count:
    if count[x]==5:
        answer='YES'
print(answer)
