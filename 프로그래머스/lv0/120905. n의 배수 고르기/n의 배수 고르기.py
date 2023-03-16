def solution(n, numlist):
    answer = []
    for x in numlist:
        if not x%n: answer.append(x)
    return answer