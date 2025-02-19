import sys
input=sys.stdin.readline

def toNum(r,c):
   return r*m+c

def find(a):
   if p[a]<0: return a
   p[a]=find(p[a])
   return p[a]

def union(a,b):
   a,b=find(a),find(b)
   if a!=b:p[b]=a

def kruskal():
   result=0
   cnt=0
   limit=n*m-1
   for c,a,b in graph:
      a,b=find(a),find(b)
      if a!=b:
         cnt+=1
         result+=c
         union(a,b)
         if cnt==limit: return result
         

for tt in range(int(input())):
   n,m=map(int,input().split())
   graph=[]
   for i in range(n):
      temp=tuple(map(int,input().split()))
      for j in range(m-1):
         graph.append((temp[j],toNum(i,j),toNum(i,j+1)))
   for i in range(n-1):
      temp=tuple(map(int,input().split()))
      for j in range(m):
         graph.append((temp[j],toNum(i,j),toNum(i+1,j)))

   graph.sort()
   p=[-1]*(n*m)
   print(kruskal())
