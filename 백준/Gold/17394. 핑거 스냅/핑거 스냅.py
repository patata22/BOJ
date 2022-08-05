from collections import deque

def sol(n):
    q=deque()
    q.append(n)
    visited=[0]*3000001
    visited[n]=1
    t=0
    while q:
        for _ in range(len(q)):
            now= q.popleft()
            if a<=now<=b and isPrime[now]:return t
            if not visited[now//2]:
                visited[now//2]=1
                q.append(now//2)
            if not visited[now//3]:
                visited[now//3]=1
                q.append(now//3)
            if now>0 and not visited[now-1]:
                visited[now-1]=1
                q.append(now-1)
            if now<3000000 and not visited[now+1]:
                visited[now+1]=1
                q.append(now+1)
            
        t+=1
    return -1

def sieve():
    for i in range(2,100001):
        if isPrime[i]:
            for j in range(i+i,100001,i):
                isPrime[j]=0
                
isPrime=[1]*100001
isPrime[0]=0
isPrime[1]=0

sieve()

for _ in range(int(input())):
    n,a,b=map(int,input().split())
    print(sol(n))
