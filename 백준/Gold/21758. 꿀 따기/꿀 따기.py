n=int(input())
number=list(map(int,input().split()))
total=sum(number)
answer1= total-number[0]-number[-1]+max(number[1:n-1])

temp=number[:]
for i in range(n-2,-1,-1):
    temp[i]+=temp[i+1]
a=0
for i in range(1,n):
    a=max(a,temp[i]-2*number[i])
answer2= temp[0]-number[0]+a

temp=number[:]
for i in range(1,n):
    temp[i]+=temp[i-1]
a=0
for i in range(n-1):
    a=max(a,temp[i]-2*number[i])
answer3 = temp[-1]-number[-1]+a
print(max(answer1,answer2,answer3))
