def solution(n):
    answer = 1 if n**0.5 == int(n**0.5) else 2
    return answer