import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        p[b]+=p[a]
        capa[b]+=capa[a]
        capa[a]=0
        p[a]=b


n,l=map(int,input().split())
p=[-1]*(l+1)
capa=[0]*(l+1)
for _ in range(n):
    a,b=map(int,input().split())
    union(a,b)
    root=find(a)
    if capa[root]<-p[root]:
        capa[root]+=1
        print('LADICA')
    else:
        print('SMECE')

