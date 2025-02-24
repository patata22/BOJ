input()
temp=list(map(int,input()))
answer=0
while len(temp)>1:
   if temp[-1]==0: temp.pop()
   else:
      answer+=1
      temp.pop()
      flag=False
      while temp and temp[-1]==1:
         temp.pop()
      if temp: temp.pop()
      temp.append(1)

print(answer)
