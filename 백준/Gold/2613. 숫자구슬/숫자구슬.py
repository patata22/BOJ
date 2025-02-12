def sol():
   l=1
   r=30001
   while l+1<r:
      mid=(l+r)//2
      result=check(mid)
      if result[0]==True:
         r=mid
         lst=result[1]
      else: l=mid
   print(r)
   
   temp=[]
   for i in range(1,len(lst)):
      temp.append(lst[i]-lst[i-1])
   answer=[]
   cnt=m-len(temp)
   while temp:
      if cnt==0 or temp[-1]==1: answer.append(temp.pop())
      else:
         answer.append(1)
         temp[-1]-=1
         cnt-=1
   answer=answer[::-1]
   print(*answer)

def check(mid):
   idx=0
   total=0
   group=[0]
   cnt=0
   while idx+1<=n:
      idx+=1
      if number[idx]>mid: return (False, [])
      if total+number[idx]>mid:
         group.append(idx-1)
         total=number[idx]
         cnt+=1
         continue
      total+=number[idx]
   if total:
      cnt+=1
      group.append(n)
   return (cnt<=m,group)
      

n,m=map(int,input().split())
number=[0]+list(map(int,input().split()))
sol()
