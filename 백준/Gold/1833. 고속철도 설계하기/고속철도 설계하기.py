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
    global cost,count
    additional=0
    connect=[]
    for a,b,c in graph:
        A,B=find(a),find(b)
        if A!=B:
            count+=1
            additional+=1
            cost+=c
            union(A,B)
            connect.append((a+1,b+1))
            if count==n-1:break
    print(cost,additional)
    for x in connect:print(*x)
            
n=int(input())
cost=0
count=0
graph=[]
p=[-1]*n
temp=[list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        if temp[i][j]<0:
            cost-=temp[i][j]
            if find(i)!=find(j):
                count+=1
                union(i,j)
        else:
            graph.append((i,j,temp[i][j]))
graph.sort(key=lambda x: x[2])       
sol()