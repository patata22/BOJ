from collections import deque

def sol():
    global answer
    q=deque()
    q.append(n)
    visited.add((int(''.join(n)),0))
    t=1
    while q and t<=k:
        changed=False
        for _ in range(len(q)):
            now=q.popleft()
            for i in range(l):
                for j in range(i+1,l):
                    if i==0 and now[j]=='0': continue
                    new = now[:]
                    new[i],new[j]=new[j],new[i]
                    temp=int(''.join(new))
                    changed=True
                    if (temp, t%2) not in visited:
                        if t%2==k%2:
                            answer=max(temp,answer)
                        visited.add((temp, t%2))
                        q.append(new)
        if not changed:
            answer=-1
            break
        t+=1
    


n,k=input().split()
k=int(k)
n=list(n)
N=int(''.join(n))
l=len(n)
visited=set()
answer=-1
if k%2==0: answer=N
if l==2 and N%10==0: answer=-1
sol()
print(answer)
