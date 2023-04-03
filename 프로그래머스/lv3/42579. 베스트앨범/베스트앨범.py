import heapq

def solution(genres, plays):
    answer = []
    
    n=len(genres)
    count={}
    count_rank={}
    for genre in genres:
        count[genre]=0
        count_rank[genre]=[]
        
    for i in range(n):
        genre=genres[i]
        count[genre]+=plays[i]
        heapq.heappush(count_rank[genre],(-plays[i],i))
    
    q=[]
    for genre in count:
        q.append((-count[genre], genre))
    q.sort()
    for c,name in q:
        target = count_rank[name]
        answer.append(heapq.heappop(target)[1])
        if target: answer.append(heapq.heappop(target)[1])
    return answer