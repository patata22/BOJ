import sys
input=sys.stdin.readline

n=int(input())
line=[tuple(map(int,input().split())) for i in range(n)]
line.sort()

answer=0
s,e=line[0]
for i in range(1,n):
    l,r=line[i]
    if s<=l<=e: e=max(e,r)
    elif l>e:
        answer+=e-s
        s,e=l,r
answer+=e-s
print(answer)
   