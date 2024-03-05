import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b:p[b]=a
        
for tt in range(int(input())):
    if tt:print()
    print(f'Scenario {tt+1}:')
    n=int(input())
    p=[-1]*n
    for _ in range(int(input())):
        a,b=map(int,input().split())
        union(a,b)
    for _ in range(int(input())):
        a,b=map(int,input().split())
        print(int(find(a)==find(b)))
