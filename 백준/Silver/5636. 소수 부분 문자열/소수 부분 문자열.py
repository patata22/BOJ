isPrime=[1]*100001
isPrime[0]=0
isPrime[1]=0
for i in range(2,100001):
    if isPrime[i]:
        for j in range(i+i,100001,i):
            isPrime[j]=0


while True:
    temp=input()
    if temp=='0': break
    answer=0
    n=len(temp)
    for i in range(n):
        for j in range(1,7):
            if i+j>n: break
            x=int(temp[i:i+j])
            if x<=100000 and isPrime[x]:answer=max(x,answer)
    print(answer)
