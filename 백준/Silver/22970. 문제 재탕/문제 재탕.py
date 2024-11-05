n=int(input())
number=list(map(int,input().split()))
up=[1]*n
down=[1]*n

for i in range(1,n):
    if number[i]>number[i-1]: up[i]=up[i-1]+1
for i in range(n-2,-1,-1):
    if number[i]>number[i+1]: down[i]=down[i+1]+1

answer=0
for i in range(n):
    answer=max(answer,up[i]+down[i])

print(answer-1)