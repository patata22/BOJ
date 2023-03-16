def solution(n):
    answer = []
    for i in range(1,n+1):
        if not n%i: answer.append(i)
    return answer