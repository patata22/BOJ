import sys
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

p=[-1]*(1000001)

for _ in range(int(input())):
    cmd=input().split()
    if cmd[0]=='I':
        a,b=int(cmd[1]), int(cmd[2])
        union(a,b)
    else:
        result=find(int(cmd[1]))
        print(-p[result])
