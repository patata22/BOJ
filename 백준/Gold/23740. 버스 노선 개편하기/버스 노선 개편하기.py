import sys
input=sys.stdin.readline

n=int(input())
bus=[tuple(map(int,input().split())) for i in range(n)]
bus.sort(key=lambda x: x[0])
answer=[]
l=bus[0][0]
r=bus[0][1]
cost=bus[0][2]
for i in range(1,n):
    s,e,c = bus[i]
    if s<=r:
        r=max(r,e)
        cost=min(cost,c)
    else:
        answer.append((l,r,cost))
        l,r,cost=s,e,c
answer.append((l,r,cost))
print(len(answer))
for x in answer:print(*x)