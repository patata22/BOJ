def solution(array):
    answer = 0
    for x in map(str, array):
        answer+=x.count('7')
    
    return answer