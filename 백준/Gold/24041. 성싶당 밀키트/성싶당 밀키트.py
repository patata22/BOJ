import sys
input=sys.stdin.readline

def sol():
    l=0
    r=2*(10**9)+1
    while l+1<r:
        mid= (l+r)//2
        if para(mid): l=mid
        else: r= mid
    return l

def para(mid):
    total=0
    for s,l in important:
        total+=s*max(1,mid-l)
    temp=[]
    for s,l in option:
        tt=s*max(1,mid-l)
        total+=tt
        temp.append(tt)
    temp.sort()
    for _ in range(k):
        total-=temp.pop()
    
    return total<=g

n,g,k=map(int,input().split())
important=[]
option=[]
for _ in range(n):
    s,l,o=map(int,input().split())
    if o: option.append((s,l))
    else: important.append((s,l))
k=min(k,len(option))
    
print(sol())
