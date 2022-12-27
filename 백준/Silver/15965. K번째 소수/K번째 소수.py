def sieve():
    for i in range(2,10**7):
        if isPrime[i]:
            prime.append(i)
            for j in range(i+i, 10**7, i):
                isPrime[j]=0
    

prime = []
isPrime = [1]*(10**7)
sieve()
print(prime[int(input())-1])
