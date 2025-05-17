n=int(input())
number=tuple(map(int,input().split()))
odd=[]
even=[]
for i in range(n):
    if number[i]%2: odd.append(i)
    else: even.append(i)

idx=0
answer1=0
answer2=0
for x in odd:
    answer1+=x-idx
    idx+=1
idx=0
for x in even:
    answer2+=x-idx
    idx+=1
print(min(answer1,answer2))