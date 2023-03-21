import heapq

def solution(storey):
    answer = float('inf')
    def dfs(now, count):
        nonlocal answer
        if now<10:
            answer=min(answer,count+now, count+10-now+1)
            return
        nxt=now//10
        temp = now%10
        dfs(nxt,count+temp)
        dfs(nxt+1,count+10-temp)
    
    dfs(storey, 0)
    return answer
