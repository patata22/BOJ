input()
x=list(input())
now='IO'
answer=0
for i in range(len(x)):
   if x[i]!=now[i%2]:
      answer+=1
print(answer)
