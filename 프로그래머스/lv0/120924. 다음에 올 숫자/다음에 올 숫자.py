def solution(common):
    if common[-1]-common[-2]==common[-2]-common[-3]:
        answer = 2*common[-1]-common[-2]
    else:
        answer = (common[-1]**2)//common[-2]
    return answer