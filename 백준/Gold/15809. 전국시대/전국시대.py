import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    p[a]+=p[b]
    p[b]=a

def war(a,b):
    a,b=find(a),find(b)
    A,B=-p[a], -p[b]
    if A>B:
        p[a]-=p[b]
        p[b]=a
        return 1
    elif A<B:
        p[b]-=p[a]
        p[a]=b
        return 1
    elif A==B:
        p[a]=-float('inf')
        p[b]=-float('inf')
        return 2


n,m=map(int,input().split())
p=[-int(input()) for i in range(n)]
count=n
for _ in range(m):
    a,b,c = map(lambda x: int(x)-1, input().split())
    if a==0:
        union(b,c)
        count-=1
    else:
        count-=war(b,c)
    


answer=[]
for x in p:
    if x<0 and x!=-float('inf'):
        answer.append(-x)
answer.sort()
print(count)
if answer:print(*answer)
