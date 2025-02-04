n=int(input())

number=list(map(int,input().split()))
answer=sorted(number)

odd=[]
even=[]

for i in range(n):
   if i%2==0: odd.append(number[i])
   else: even.append(number[i])

odd.sort(reverse=True)
even.sort(reverse=True)

result=[]
while even:
   result.append(odd.pop())
   result.append(even.pop())

if odd: result.append(odd.pop())

print('YES') if result==answer else print('NO')
