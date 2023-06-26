import sys
input=sys.stdin.readline

def find(a):
    if p[a]<0: return a
    p[a]=find(p[a])
    return p[a]

def union(a,b):
    a,b=find(a),find(b)
    if a!=b: p[b]=a

def connect(i,j):
    x1,y1,r1=point[i]
    x2,y2,r2=point[j]
    if (x1-x2)**2+(y1-y2)**2<=(r1+r2)**2:
        union(i,j)
        

for T in range(int(input())):
    n=int(input())
    answer=0
    p=[-1]*n
    point=[tuple(map(int,input().split())) for i in range(n)]
    for i in range(n):
        for j in range(1,n):
            connect(i,j)
    for i in range(n):
        if p[i]<0: answer+=1
    print(answer)
    
    
