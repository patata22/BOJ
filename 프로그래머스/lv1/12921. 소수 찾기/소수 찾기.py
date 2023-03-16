def solution(n):
    isPrime = [1]*(n+1)
    isPrime[0]=0
    isPrime[1]=0
    for i in range(2,n+1):
        if isPrime[i]:
            for j in range(i+i,n+1,i):
                isPrime[j]=0
    return sum(isPrime)
