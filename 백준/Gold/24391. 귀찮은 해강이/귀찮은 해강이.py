import sys
input=sys.stdin.readline

def find(a):
     if p[a]<0: return a
     p[a]=find(p[a])
     return p[a]

def union(a,b):
     a,b=find(a),find(b)
     if a!=b: p[b]=a

n,m=map(int,input().split())
p=[-1]*(n+1)

for _ in range(m):
     a,b=map(int,input().split())
     union(a,b)

number= tuple(map(int,input().split()))
answer=0
for i in range(n-1):
     if find(number[i])!=find(number[i+1]):answer+=1
print(answer)
