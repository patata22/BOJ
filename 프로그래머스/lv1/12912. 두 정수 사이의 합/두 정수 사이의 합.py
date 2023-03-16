def solution(a, b):
    if a>b:
        a,b=b,a
    answer = total(b)-total(a-1)
    return answer


def total(n):
    return (n*(n+1))//2