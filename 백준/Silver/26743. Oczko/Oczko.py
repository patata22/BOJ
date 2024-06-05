from collections import deque

def calc():
    q=deque()
    q.append(0)
    for x in cards:
        for _ in range(len(q)):
            now=q.popleft()
            if x.isnumeric() and now+int(x)<=21: q.append(now+int(x))
            else:
                if x=='A':
                    if now+1<=21: q.append(now+1)
                    if now+11<=21: q.append(now+11)
                else:
                    if now+10<=21: q.append(now+10)
    if not q:return -1
    
    else: return max(q)

n=int(input())

answer=[]
high=0
for i in range(1,n+1):
    cards=list(input())
    score=calc()
    if score>high:
        answer=[i]
        high=score
    elif score==high:
        answer.append(i)

print(len(answer))
if answer:print(*answer)