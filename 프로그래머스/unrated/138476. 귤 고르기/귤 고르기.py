from collections import Counter
def solution(k, tangerine):
    count= Counter(tangerine)
    tangerine=sorted(list(set(tangerine)), key= lambda x: count[x])
    answer=0
    total=0
    while total<k:
        answer+=1
        total+=count[tangerine.pop()]
    return answer