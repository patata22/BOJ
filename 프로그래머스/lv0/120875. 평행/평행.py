def solution(dots):
    a,b,c,d=dots
    answer=0
    if calc(a,b,c,d) or calc(a,c,b,d) or calc(a,d,b,c): answer=1
    return answer

def calc(dot1, dot2, dot3, dot4):
    x1,y1=dot1
    x2,y2=dot2
    a1,b1=dot3
    a2,b2=dot4
    return abs(y2-y1)*abs(a2-a1)==abs(b2-b1)*abs(x2-x1)
