def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    while d:
        x=d.pop()
        if budget-x>=0:
            budget-=x
            answer+=1
        else: break
    return answer