n,k=map(int,input().split())
number=list(map(int,input().split()))
for i in range(1,n):
    number[i]+=number[i-1]
print(sum(sorted(number)[-k:]))