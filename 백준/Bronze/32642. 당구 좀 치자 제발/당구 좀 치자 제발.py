n=int(input())
number=list(map(int,input().split()))

if number[0]==0: number[0]=-1

for i in range(1,n):
    if number[i]: number[i]=number[i-1]+1
    else: number[i]=number[i-1]-1

print(sum(number))
