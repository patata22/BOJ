def solution(myString):
    a=[]
    for x in myString.split('x'):
        if x: a.append(x)
    return sorted(a)
    