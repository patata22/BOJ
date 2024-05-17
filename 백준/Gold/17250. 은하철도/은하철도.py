import sys
sys.setrecursionlimit(10**5+10)
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:
        p[a]+=p[b]
        p[b]=a

n,m=map(int,input().split())
p=[0]+[-int(input()) for i in range(n)]
answer=[]
for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)
    answer.append(str(-p[find(a)]))

print('\n'.join(answer))
    
