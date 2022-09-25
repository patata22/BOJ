from collections import deque
n=int(input())
first=deque([input() for i in range(n)])
last=deque([input() for i in range(n)])
cri=set()
answer=0
while first and last:
    
    if last[0] in cri:
        last.popleft()
        continue
    if first[0] in cri:
        first.popleft()
        continue
    if first[0]==last[0]:
        first.popleft()
        last.popleft()
    else:
        answer+=1
        cri.add(last.popleft())
print(answer)
        
