def sol():
   if not burger[0]==burger[-1]=='a': return 'No'
   for i in range(1,n):
      if burger[i]==burger[i-1]: return 'No'
   cnt=[0]*4
   for x in burger:
      cnt[ord(x)-97]+=1
   for i in range(4):
      if cnt[i]>number[i]: return 'No'
   return 'Yes'
   
n=int(input())
number=tuple(map(int,input().split()))
burger=list(input())
print(sol())