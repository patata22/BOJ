n,m=map(int,input().split())
number=[0]*(m+1)
for _ in range(n):
    temp=list(map(int,input().split()))
    for j in range(1,m+1):
        number[j]+=temp[j-1]

for i in range(1,m+1):
    number[i]+=number[i-1]

k=int(input())
answer=0
for i in range(k,m+1):
    answer=max(answer,number[i]-number[i-k])
print(answer)
