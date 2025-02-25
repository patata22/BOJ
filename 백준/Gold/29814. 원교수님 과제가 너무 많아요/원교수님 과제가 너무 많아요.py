import sys
input=sys.stdin.readline

def find(a):
   if p[a]<0: return a
   p[a]=find(p[a])
   return p[a]

def union(a,b):
   a,b=find(a),find(b)
   if a!=b:
      if a>b: a,b=b,a
      p[b]=a

n,C=map(int,input().split())
bot=[]
for _ in range(n):
   bot.append(tuple(map(int,input().split())))

p=[-1]*(n+1)
bot.sort(key=lambda x: x[2])

answer=0
total=0
while bot:
   due,need,point=bot.pop()
   start=due-need+1
   able=find(start)
   if able!=0:
      answer+=1
      total+=point
      union(able-1,able)
      if total>=C: break

if total>=C: print(answer)
else:print("I'm sorry professor Won!")