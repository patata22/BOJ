from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    q=deque([i for i in range(len(priorities))])    
    count=0
    while q:
        target=max(priorities)
        i,priority=q.popleft(), priorities.popleft()
        if priority==target:
            count+=1
            if i==location: return count
        else: 
            q.append(i)
            priorities.append(priority)