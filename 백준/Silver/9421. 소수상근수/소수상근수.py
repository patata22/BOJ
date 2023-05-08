def seive():
    for i in range(2,n+1):
        if isPrime[i]:
            for j in range(i+i, n+1, i):
                isPrime[j]=0

def isSanggun(x):
    record=set()
    while True:
        record.add(x)
        temp=0
        while x:
            temp+=(x%10)**2
            x//=10
        if temp==1: return True
        elif temp in record: return False
        x=temp

n=int(input())
isPrime=[1]*(n+1)
isPrime[0]=0
isPrime[1]=0
seive()
for i in range(1,n+1):
    if isPrime[i] and isSanggun(i): print(i)
  