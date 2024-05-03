DIV=123456789

def sieve():
    for i in range(2,MAX):
        if isPrime[i]:
            for j in range(i+i,MAX, i):
                isPrime[j]=0

n=int(input())
MAX=min(n+1,40001)
isPrime=[1]*MAX
sieve()
prime=[]
for i in range(2,MAX):
    if isPrime[i]: prime.append(i)
dp=[0]*MAX
dp[0]=1
for x in prime:
    for i in range(x,MAX):
        dp[i]=(dp[i]+dp[i-x])%DIV
    
print(dp[-1])