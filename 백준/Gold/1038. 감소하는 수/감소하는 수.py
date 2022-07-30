from collections import deque

desc=[]
q=deque()
for i in range(10):
    desc.append(i)
    q.append(i)
cnt=9
while q and cnt<=999999:
    now=q.popleft()
    temp = now%10
    for i in range(temp):
        cnt+=1
        desc.append(now*10+i)
        
        q.append(now*10+i)

n=int(input())
print(-1) if n>cnt else print(desc[n])
    

