import heapq

def solution(n, s):
    if s<n: return [-1]
    answer = [s//n]*n
    
    for _ in range(s%n):
        heapq.heappush(answer, heapq.heappop(answer)+1)
    answer.sort()
    return answer