from collections import deque

def solution(queue1, queue2):
    n=len(queue1)
    answer = -1
    
    sum1= sum(queue1)
    sum2= sum(queue2)
    q1=deque(queue1)
    q2=deque(queue2)
    for i in range(4*n):
        if sum1==sum2: return i
        elif sum1>sum2:
            x=q1.popleft()
            sum1-=x
            sum2+=x
            q2.append(x)
        elif sum2>sum1:
            x=q2.popleft()
            sum1+=x
            sum2-=x
            q1.append(x)
    return answer