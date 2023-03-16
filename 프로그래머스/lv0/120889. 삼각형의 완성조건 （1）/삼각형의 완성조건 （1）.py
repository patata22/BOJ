def solution(sides):
    sides.sort()
    a,b,c=sides
    answer= 1 if a+b>c else 2
    return answer