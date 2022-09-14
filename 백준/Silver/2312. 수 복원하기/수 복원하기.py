def sieve():
    for i in range(2,100001):
        if isPrime[i]:
            for j in range(i+i,100001,i):
                isPrime[j]=0

isPrime=[1]*(100001)
isPrime[0]=0
isPrime[1]=0
sieve()
for _ in range(int(input())):
    n=int(input())
    answer=[0]*(n+1)
    while not isPrime[n]:
        for i in range(2,n+1):
            if n%i==0:
                answer[i]+=1
                n//=i
                break
    answer[n]+=1
    for i in range(2,n+1):
        if answer[i]: print(i,answer[i])
