from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    bridge=deque([0]*bridge_length)
    trucks=truck_weights[::-1]
    totalweight=trucks.pop()
    bridge[-1]=totalweight
    answer = 1
    while totalweight or trucks:
        answer+=1
        totalweight-=bridge.popleft()
        if trucks and totalweight+trucks[-1]<=weight:
            totalweight+=trucks[-1]
            bridge.append(trucks.pop())
        else: bridge.append(0)
    
    return answer