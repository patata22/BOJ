def solution(order):
    answer = 0
    for x in str(order):
        if x in ('3','6','9'): answer+=1
    return answer