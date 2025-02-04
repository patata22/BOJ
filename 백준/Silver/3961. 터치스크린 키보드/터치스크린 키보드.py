keyboard=[]
keyboard.append('qwertyuiop')
keyboard.append('asdfghjkl;')
keyboard.append('zxcvbnm,./')
distance={}

for i in range(3):
   for j in range(10):
      now=keyboard[i][j]
      for k in range(3):
         for l in range(10):
            nxt=keyboard[k][l]
            distance[(now,nxt)]=abs(i-k)+abs(j-l)
   
for tt in range(int(input())):
   ori,n = input().split()
   n=int(n)
   result=[]
   for _ in range(n):
      temp=input()
      dist=0
      for _ in range(len(ori)):
         dist+=distance[(ori[_],temp[_])]
      result.append((temp,dist))
   result.sort(key=lambda x: (x[1],x[0]))

   for x in result:
      print(*x)
