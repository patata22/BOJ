def solution(emergency):
    answer=[]
    e=sorted(emergency, reverse=True)
    for x in emergency:
        answer.append(e.index(x)+1)
    return answer