def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score)>=m:
        for _ in range(m-1):score.pop()
        answer+=m*score.pop()
    return answer