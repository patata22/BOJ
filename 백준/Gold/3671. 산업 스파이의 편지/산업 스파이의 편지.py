def seive():
    for i in range(2,10000000):
        if isPrime[i]:
            for j in range(i+i,10000000,i):
                isPrime[j]=0
    
isPrime=[1]*10000000
isPrime[0]=0
isPrime[1]=0
seive()
def sol(depth,num):
    if isPrime[num]:prime.add(num)
    if depth==n:
        return
    for i in range(n):
        if not used[i]:
            used[i]=1
            sol(depth+1,10*num+temp[i])
            used[i]=0
    

for _ in range(int(input())):
    temp=list(map(int,input()))
    n=len(temp)
    used=[0]*n
    prime=set()
    sol(0,0)
    print(len(prime))    
