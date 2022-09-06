def sieve():
    for i in range(2,1000001):
        if isPrime[i]:
            for j in range(i+i,1000001,i):
                isPrime[j]=0
isPrime=[1]*1000001
isPrime[1]=0
sieve()
n,m=map(int,input().split())
for i in range(n,m+1):
    if isPrime[i]:print(i)
    
