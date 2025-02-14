import sys
input=sys.stdin.readline

def check(x1,y1,x2,y2):
   return (x1-x2)**2+(y1-y2)**2<=r**2

def sol(depth,start,result):
   if depth==d:
      global answer
      answer=max(answer,result)
      return
   for i in range(start,n):
      temp=0
      v=[]
      x1,y1=restaurant[i]
      for j in range(m):
         x2,y2,p=point[j]
         if not visited[j] and check(x1,y1,x2,y2):
            visited[j]=1
            v.append(j)
            temp+=p
      sol(depth+1,i+1,result+temp)
      for x in v: visited[x]=0

d,r=map(int,input().split())

n=int(input())
restaurant=[tuple(map(int,input().split())) for i in range(n)]
m=int(input())
point=[tuple(map(int,input().split())) for i in range(m)]

visited=[0]*m

answer=0

sol(0,0,0)
print(answer)
