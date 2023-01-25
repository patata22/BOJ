def sieve():
    for i in range(2,1000001):
        if isPrime[i]:
            prime.append(i)
            for j in range(i+i,1000001,i):
                isPrime[j]=0
    
prime= []
isPrime=[1]*(1000001)
isPrime[0]=0
isPrime[1]=0
sieve()

for _ in range(int(input())):
    n=int(input())
    count = 0
    for i in prime:
        if i > n//2:
            break
        if isPrime[n-i]:
            count += 1
    print(count)