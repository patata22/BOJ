isPrime=[1]*320000
isPrime[0]=0
isPrime[1]=0
prime=[]
for i in range(2,320000):
    if isPrime[i]:
        prime.append(i)
        for j in range(i+i,320000,i):
            isPrime[j]=0
answer=[]
for i in range(1,len(prime)+1):
    if isPrime[i]:
        answer.append(prime[i-1])
for _ in range(int(input())):
    print(answer[int(input())-1])
    

