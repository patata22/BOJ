import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    global answer
    a,b=find(a),find(b)
    if a!=b:
        if size[a]<rain[a]:
            answer+=p[a]
        if size[b]<rain[b]:
            answer+=p[b]
        if size[a]+size[b]<rain[a]+rain[b]:
            answer-=p[a]+p[b]
        p[a]+=p[b]
        p[b]=a
        size[a]+=size[b]
        rain[a]+=rain[b]
        
n,m=map(int,input().split())

p=[-1]*n
size=list(map(int,input().split()))
rain=list(map(int,input().split()))

answer=0
for i in range(n):
    if rain[i]>size[i]: answer+=1


for _ in range(m):
    temp=list(map(int,input().split()))
    q=temp[0]
    if q==1:
        union(temp[1]-1,temp[2]-1)
    elif q==2:
        print(answer)
