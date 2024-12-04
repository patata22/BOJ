def seive():
    for i in range(2,77778):
        if isPrime[i]:
            prime.append(i)
            for j in range(i+i,77778,i):
                isPrime[j]=0

def calc(n):
    odd=[]
    for x in prime:
        if x>n:break
        if n%x==0:
            cnt=0
            while n%x==0:
                n//=x
                cnt+=1
            if cnt%2: odd.append(x)
    return tuple(odd)
        

prime=[]
isPrime=[1]*77778
seive()
countA={}
countB={}

a,b=map(int,input().split())
if a>b: a,b=b,a
for i in range(1,a+1):
    temp=calc(i)
    if temp not in countA: countA[temp]=0
    if temp not in countB: countB[temp]=0
    countA[temp]+=1
    countB[temp]+=1

for i in range(a+1,b+1):
    temp=calc(i)
    if temp not in countB: countB[temp]=0
    countB[temp]+=1

answer=0
for x in countA:
    answer+=countA[x]*countB[x]

print(answer)