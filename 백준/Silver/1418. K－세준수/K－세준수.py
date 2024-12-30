def seive():
    for i in range(2,100001):
        if not prime[i]:
            for j in range(i,100001,i):
                prime[j]=i
prime=[0]*100001
prime[1]=1
seive()
n=int(input())
k=int(input())
answer=0
for i in range(1,n+1):
    if prime[i]<=k: answer+=1
print(answer)