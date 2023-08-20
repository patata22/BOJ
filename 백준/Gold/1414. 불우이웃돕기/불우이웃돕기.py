from collections import deque

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a), find(b)
    if a!=b:p[b]=a

def kruskal():
    global total
    cnt=0
    for c,x,y in graph:
        
        if find(x)!=find(y):
            cnt+=1
            total-=c
            union(x,y)
            if cnt==2*n-1: return 1
    return -1
            
n=int(input())
p=[-1]*2*n
graph= []
total = 0

for x in range(n):
    temp=input()
    graph.append((0,x,x+n))
    for y in range(n):
        z=temp[y]
        if z.islower():
            graph.append((ord(z)-96,x,y))
            total+=ord(z)-96
        elif z.isupper():
            graph.append((ord(z)-38,x,y))
            total+=ord(z)-38

graph.sort()
answer=kruskal()
if answer<0: print(-1)
else: print(total)
