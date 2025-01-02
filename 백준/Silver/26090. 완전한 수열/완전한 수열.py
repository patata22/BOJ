isPrime=[1]*1000001
isPrime[0]=0
isPrime[1]=0
for i in range(2,1000001):
    if isPrime[i]:
        for j in range(i+i,1000001,i):
            isPrime[j]=0
    
n=int(input())
number=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    number[i]+=number[i-1]

answer=0
for i in range(n+1):
    for j in range(i):
        if not isPrime[(i-j)]: continue
        temp=number[i]-number[j]
        if isPrime[temp]: answer+=1

print(answer)
