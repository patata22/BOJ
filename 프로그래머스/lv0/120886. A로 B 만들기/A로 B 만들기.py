def solution(before, after):
    answer=1 if sorted(list(before))==sorted(list(after)) else 0
    return answer