import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b,add):
    global answer
    a,b=find(a), find(b)
    if a!=b:
        if add: answer+=p[a]*p[b]
        p[b]+=p[a]
        p[a]=b


n,m,q=map(int,input().split())
p=[-1]*(n+1)
graph=[(0,0)]+[list(map(int,input().split())) for i in range(m)]
cut=[int(input()) for i in range(q)]
temp=set(cut)
answer=0
for i in range(1,m+1):
    if i in cut: continue
    a,b=graph[i]
    union(a,b,False)
while cut:
    a,b=graph[cut.pop()]
    union(a,b,True)
print(answer)
