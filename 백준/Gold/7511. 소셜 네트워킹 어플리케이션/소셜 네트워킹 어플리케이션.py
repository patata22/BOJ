import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    pa=find(a)
    pb=find(b)
    if pa!=pb: p[pb]=pa

for t in range(int(input())):
    if t:print()
    print(f'Scenario {t+1}:')
    n=int(input())
    p=[-1]*n
    for _ in range(int(input())):
        a,b=map(int,input().split())
        union(a,b)
    for _ in range(int(input())):
        a,b=map(int,input().split())
        if find(a)==find(b):print(1)
        else: print(0)
