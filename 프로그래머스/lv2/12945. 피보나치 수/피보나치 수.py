def solution(n):
    DIV=1234567
    x,y=0,1
    for i in range(n):
        x,y=y,(x+y)%DIV
    return x