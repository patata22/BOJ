from collections import deque

def sol():
    q=deque()
    for i in range(1,10):q.append(str(i))
    while len(answer)<1000000:
        now=q.popleft()
        for i in range(10):
            flag=True
            for x in now:
                if int(x)==i:
                    flag=False
                    break
            if flag:
                q.append(now+str(i))
                answer.append(int(now+str(i)))
        
    

answer=[1,2,3,4,5,6,7,8,9]
sol()
while True:
    x=int(input())
    if x==0: break
    else: print(answer[x-1])
