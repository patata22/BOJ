def solution(a,b):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    while a:
        answer+=a.pop()*b.pop()
    return answer