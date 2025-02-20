n=int(input())
number=list(map(int,input().split()))
target=sorted(number)
idx={}
for i in range(n):
   idx[number[i]]=i

answer=0
for i in range(n):
   if number[i]!=target[i]:
      answer+=1
      temp=idx[target[i]]
      idx[number[i]]=temp
      number[temp]=number[i]
print(answer)