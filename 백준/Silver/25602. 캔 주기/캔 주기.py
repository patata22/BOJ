def sol(day,total):
   if day==k:
      global answer
      answer=max(answer,total)
      return
    
   for i in range(n):
      if can[i]:
         can[i]-=1
         for j in range(n):
            if can[j]:
               can[j]-=1
               sol(day+1, total+score1[day][i]+score2[day][j])
               can[j]+=1
         can[i]+=1
   
n,k=map(int,input().split())

can=list(map(int,input().split()))
score1=[list(map(int,input().split())) for i in range(k)]
score2=[list(map(int,input().split())) for i in range(k)]

answer=0

sol(0,0)
print(answer)