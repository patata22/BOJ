def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0: return False
    return True

prime=[1]*50001
prime[1]=0
for i in range(2,50001):
    if prime[i]:
        if isPrime(i):
            for j in range(2*i,50001,i):
                prime[j]=0
P=[i for i in range(2,50001) if prime[i]]
mul=[]
for x in P:
    for y in P:
        if x==y or x*y>100001:continue
        mul.append(x*y)        

mul.sort()
for _ in range(int(input())):
    n=int(input())
    for x in mul:
        if x>=n:
            print(x)
            break
    