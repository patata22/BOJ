import sys
input=sys.stdin.readline

for tt in range(int(input())):
   n,k=map(int,input().split())
   attack=tuple(map(int,input().split()))
   defence=tuple(map(int,input().split()))
   temp=[]
   A=0
   D=0
   acnt=n
   dcnt=0
   answer=0
   for i in range(n):
      temp.append((attack[i],defence[i]))
      A+=attack[i]
   temp.sort(key=lambda x: x[1]-x[0])
   
   while temp:
      a,d=temp.pop()
      A-=a
      D+=d
      acnt-=1
      dcnt+=1
      if abs(acnt-dcnt)<=k: answer=max(answer,A+D)

   print(answer)
