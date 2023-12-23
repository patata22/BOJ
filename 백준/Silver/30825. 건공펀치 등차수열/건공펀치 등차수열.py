n,k=map(int,input().split())
number=list(map(int,input().split()))
target=[0]*n
target[0]=number[0]
for i in range(1,n):
    target[i]=max(number[i],target[i-1]+k)
for i in range(n-2,-1,-1):
    target[i]=target[i+1]-k
answer=0
for i in range(n):
    answer+=target[i]-number[i]  
print(answer)