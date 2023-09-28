n=int(input())
number=tuple(map(int,input().split()))
total=0
for i in range(n):
    if i%2: total+=number[i]
    else: total-=number[i]

if n<=3:
    if total>=0: print(abs(total))
    else:print(-1)
else:print(abs(total))
   