def solution(numbers):
    
    n=len(numbers)
    prime=set()
    used=[0]*n
    isPrime=[1]*10000000
    isPrime[0]=0
    isPrime[1]=0
    for i in range(2,1000000):
        if isPrime[i]:
            for j in range(i*2, 10000000, i):
                isPrime[j]=0
    
    
    
    def makeNumber(count, now):
        if count==n:
            if now and isPrime[int(now)]:
                prime.add(int(now))
            return
        makeNumber(count+1, now)
        for i in range(n):
            if not used[i]:
                used[i]=1
                makeNumber(count+1, now+numbers[i])
                used[i]=0
    makeNumber(0,"")
    return len(prime)