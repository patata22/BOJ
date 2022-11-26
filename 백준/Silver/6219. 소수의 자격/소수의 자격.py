def sieve():
    for i in range(2,4000001):
        if isPrime[i]:
            for j in range(i+i, 4000001, i):
                isPrime[j] = 0
                
def check(x):
    while x:
        if x%10==d:return 1
        x//=10
    return 0
a,b,d = map(int,input().split())

isPrime = [1]*4000001
isPrime[1]=0
sieve()
answer=0
for i in range(a,b+1):
    if isPrime[i]:answer+=check(i)

print(answer)
    
