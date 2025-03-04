import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:p[b]=a

def sol():
    result=0
    cnt=0
    for a,b,c in graph:
        if find(a)!=find(b):
            union(a,b)
            cnt+=1
            result+=c
            if cnt==n: return result
        
n,m=map(int,input().split())
graph=[tuple(map(int,input().split())) for i in range(m)]    
temp=tuple(map(int,input().split()))
for i in range(n):
    graph.append((0,i+1,temp[i]))

graph.sort(key=lambda x: x[2])
p=[-1]*(n+1)

print(sol())