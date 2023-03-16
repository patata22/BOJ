def solution(score):
    answer = []
    nxt = list(map(sum,score))
    nxt.sort(reverse=True)
    for x in score:
        answer.append(nxt.index(sum(x))+1)
    return answer