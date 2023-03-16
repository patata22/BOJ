def solution(array):
    
    temp = sorted(enumerate(array), key=lambda x: x[1])
    answer=temp[-1]
    return [answer[1],answer[0]]
