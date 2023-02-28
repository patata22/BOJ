from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
number=sorted([int(input()) for i in range(n)])
answer=-1
tri = deque()
for i in range(3):
    tri.append(number.pop())

if tri[0]<tri[1]+tri[2]:
        answer=sum(tri)

while number:
    if tri[0]<tri[1]+tri[2]:
        answer=sum(tri)
        break
    else:
        tri.popleft()
        tri.append(number.pop())

if tri[0]<tri[1]+tri[2]:
        answer=sum(tri)
print(answer)
