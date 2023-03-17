import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    
    while len(scoville)>1 and scoville[0]<K:
        answer+=1
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        
    if scoville[0]<K: return -1

    return answer