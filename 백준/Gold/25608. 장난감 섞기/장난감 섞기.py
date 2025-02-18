def checkLeft(num):
   temp=[0]+num[:]
   result=0
   for i in range(1,m+1):
      temp[i]+=temp[i-1]
      result=max(result,temp[i])
   return result

def checkRight(num):
   temp=num[:]
   temp.append(0)
   result=0
   for i in range(m-1,-1,-1):
      temp[i]+=temp[i+1]
      result=max(result,temp[i])
   return result

def checkPrefix(num):
   now=num[0]
   result=num[0]
   for i in range(1,m):
      now=max(num[i],now+num[i])
      result=max(result,now)
   return result
   
def sol(depth,total):
   if depth==n:
      global answer1
      answer1=max(answer1,total)
      return
   for i in range(n):
      if not used[i]:
         used[i]=1
         sol(depth+1,total+mid[i])
         used[i]=0
         
n,m=map(int,input().split())
answer1=0
answer2=0
left=[0]*n
right=[0]*n
mid=[0]*n
used=[0]*n
for i in range(n):
   temp=list(map(int,input().split()))
   mid[i]=max(mid[i],sum(temp))
   left[i]=checkLeft(temp)
   right[i]=checkRight(temp)
   answer2=max(answer2,checkPrefix(temp))

for i in range(n):
   if not used[i]:
      used[i]=1
      for j in range(i+1,n):
         if not used[j]:
            used[j]=1
            sol(2,left[i]+right[j])
            sol(2,left[j]+right[i])
            used[j]=0
      used[i]=0

print(max(answer1,answer2))
