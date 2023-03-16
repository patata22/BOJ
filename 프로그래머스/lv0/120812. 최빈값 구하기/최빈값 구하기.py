def solution(array):
    m=0
    for x in set(array):
        if array.count(x)>m:
            m=array.count(x)
            answer=x
        elif array.count(x)==m:
            answer=-1
    return answer