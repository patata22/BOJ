import sys
input=sys.stdin.readline

toNum={}
temp=['oqz','ij','abc','def','gh','kl','mn','prs','tuv','wxy']

for i in range(10):
   for x in temp[i]:
      toNum[x]=str(i)


number='-'+input().rstrip()
n=len(number)

toWord={}

for _ in range(int(input())):
   original=input().rstrip()
   num=[]
   flag=True
   for x in original:
      try:
         num.append(toNum[x])
      except KeyError:
         flag=False
   if flag:
      num=''.join(num)
      toWord[num]=original

dp=[[float('inf'),-1,''] for i in range(n)]
dp[0]=[0,0,'']

for r in range(1,n+1):
   for l in range(1,r):
      temp=number[l:r]
      if temp in toWord:
         cnt=dp[l-1][0]+1
         if cnt<dp[r-1][0]:
            dp[r-1]=[cnt,l-1,toWord[temp]]

      
if dp[-1][0]==float('inf'):
   print(0)
   print('No solution.')
else:
   answer=[]
   now=n-1
   while now!=0:
      answer.append(dp[now][2])
      now=dp[now][1]
   print(len(answer))
   while answer:print(answer.pop())
   
