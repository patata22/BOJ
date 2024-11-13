import sys
input=sys.stdin.readline

def seive():
    for i in range(2,5000001):
        if isPrime[i]:
            for j in range(i+i,5000001,i):
                isPrime[j]=0
            
isPrime=[1]*5000001
isPrime[0]=0
seive()
for i in range(1,5000001):
    isPrime[i]+=isPrime[i-1]

n,m=map(int,input().split())
for _ in range(m):
    a,b=map(int,input().split())
    print(isPrime[b]-isPrime[a-1])

