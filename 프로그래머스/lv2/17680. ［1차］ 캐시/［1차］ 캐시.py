def solution(cacheSize, cities):
    n=len(cities)
    answer = 0
    cache= {}
    for i in range(n):
        city = cities[i].lower()
        if city in cache:
            answer+=1
            cache[city]=i
        else:
            answer+=5
            cache[city]=i
            if len(cache)>=cacheSize+1:
                temp=float('inf')
                target=0
                for x in cache:
                    if temp>cache[x]:
                        temp=cache[x]
                        target=x
                cache.pop(target)
                
    return answer