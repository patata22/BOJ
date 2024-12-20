n=int(input())
isPrime=[1]*(n+1)
prime=[]
answer=0
for i in range(2,n+1):
    if isPrime[i]:
        prime.append(i)
        for j in range(i+i,n+1,i):
            if isPrime[j]:answer+=i
            isPrime[j]=0
print(answer+sum(prime))
