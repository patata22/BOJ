def solution(arr, divisor):
    answer = []
    for x in arr:
        if not x%divisor: answer.append(x)
    answer.sort()
    if not answer: answer.append(-1)
    return answer