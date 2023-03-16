def solution(n):
    answer = 1
    now=1
    while now<n:
        answer+=1
        now*=answer
    if now>n: answer-=1
    return answer