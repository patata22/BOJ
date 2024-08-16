def sol():
    n=int(input())
    for x in prime:
        if n==1: break
        while n%x==0:
            n//=x
            cnt[x]+=1
    temp=0
    for x in prime:
        temp+=cnt[x]
    now=1
    answer=0
    
    while now<temp:
        now<<=1
        answer+=1
    return answer

isPrime=[1]*1000001
prime=[]
cnt={}
for i in range(2,1000001):
    if isPrime[i]:
        prime.append(i)
        cnt[i]=0
        for j in range(i+i,1000001,i):
            isPrime[j]=0

print(sol())