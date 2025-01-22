import sys
input=sys.stdin.readline

DIV=1000000007

def calc(x):
   if x%2==0: return x//2,1
   return (x-1)//2,x//2+1

def dq(x,n):
   if n==0: return 1
   elif n==1: return x
   temp=dq(x,n//2)
   result=(temp*temp)%DIV
   if n%2: result=(result*x)%DIV
   return result

def calcLine(line):
   now=0
   answer=1
   tile=0
   for x in unbreak[line]:
      t,a=calc(x-now-1)
      tile+=t
      answer=(answer*a)%DIV
      now=x
   t,a=calc(m-now)
   tile+=t
   answer=(answer*a)%DIV
   return tile,answer

n,m,k=map(int,input().split())
unbreak={}
for _ in range(k):
   a,b=map(int,input().split())
   if a not in unbreak: unbreak[a]=[]
   unbreak[a].append(b)

for x in unbreak: unbreak[x].sort()

tiles=0
answer=1

temp=n-len(unbreak)
t,a=calc(m)
tiles+=t*temp
answer*=dq(a,temp)


for line in unbreak:
   t,a=calcLine(line)
   tiles+=t
   answer=(answer*a)%DIV

print(tiles,answer)


