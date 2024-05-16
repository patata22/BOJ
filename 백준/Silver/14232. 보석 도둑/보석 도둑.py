def sieve():
    for i in range(2,10**6):
        if isPrime[i]:
            prime.append(i)
            for j in range(i+i,10**6,i):
                isPrime[j]=0

isPrime=[1]*(10**6)
prime=[]

sieve()
k=int(input())
answer=[]
for p in prime:
    while k%p==0:
        answer.append(p)
        k//=p
if k!=1: answer.append(k)
print(len(answer))
print(*answer)
