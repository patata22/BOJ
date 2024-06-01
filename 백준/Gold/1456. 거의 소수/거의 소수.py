a,b=map(int,input().split())
isPrime=[1]*10000001
answer=0
for i in range(2,10000001):
    if isPrime[i]:
        for j in range(i+i,10000001,i):
            isPrime[j]=0
        now=i*i
        while now<=b:
            if a<=now:answer+=1
            now*=i
print(answer)