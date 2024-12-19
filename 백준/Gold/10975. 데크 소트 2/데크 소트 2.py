from collections import deque

def sol():
    deques=[]
    for x in original:
        now=order[x]
        flag=False
        for d in deques:
            if d[0]==now+1:
                d.appendleft(now)
                flag=True
                break
            elif d[-1]==now-1:
                d.append(now)
                flag=True
                break
        if not flag:
            deques.append(deque())
            deques[-1].append(now)
    return len(deques)
                

n=int(input())
original=[int(input()) for i in range(n)]
number=sorted(original)
order={}
for i in range(n):
    order[number[i]]=i

print(sol())
