from collections import deque
import sys
input=sys.stdin.readline

def getDistance(x1,y1,x2,y2):
   return (x1-x2)**2+(y1-y2)**2


def init():
   for i in range(m):
      x1,y1=point[P[i]]
      r=R[i+1]
      for j in range(n):
         x2,y2=point[j]
         if getDistance(x1,y1,x2,y2)<=r**2:
            mark[j]=1

def sol():
   q=deque()
   result=0
   visited=[0]*n
   r=R[0]**2
   for i in range(n):
      if not mark[i]:
         q.append(point[i])
         result+=1
         visited[i]=1
   while q:
      x,y=q.popleft()
      for i in range(n):
         x2,y2=point[i]
         if not visited[i] and getDistance(x,y,x2,y2)<=r:
            visited[i]=1
            result+=1
            q.append((x2,y2))

   return result
            
n,m=map(int,input().split())
point=[tuple(map(int,input().split())) for i in range(n)]
P=list(map(lambda x: int(x)-1, input().split()))
R=list(map(int,input().split()))
mark=[0]*n
init()
print(sol())