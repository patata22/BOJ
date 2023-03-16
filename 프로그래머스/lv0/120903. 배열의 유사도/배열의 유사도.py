def solution(s1, s2):
    answer = 0
    s1,s2=set(s1), set(s2)
    for s in s1:
        if s in s2: answer+=1
    
    return answer