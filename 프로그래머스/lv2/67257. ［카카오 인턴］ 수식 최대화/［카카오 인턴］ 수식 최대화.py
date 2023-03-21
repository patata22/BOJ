def solution(expression):
    answer = []
    p=parse(expression)
    answer.append(abs(int(calc(calc(calc(p, '+'), '-'),'*')[0])))
    answer.append(abs(int(calc(calc(calc(p, '+'), '*'),'-')[0])))
    answer.append(abs(int(calc(calc(calc(p, '-'), '+'),'*')[0])))
    answer.append(abs(int(calc(calc(calc(p, '-'), '*'),'+')[0])))
    answer.append(abs(int(calc(calc(calc(p, '*'), '+'),'-')[0])))
    answer.append(abs(int(calc(calc(calc(p, '*'), '-'),'+')[0])))
    
    return max(answer)

def calc(ex, operator):
    result=[]
    i=0
    while i<len(ex):
        if ex[i]==operator:
            i+=1
            result.append(str(eval(result.pop()+operator+ex[i])))
        else: result.append(ex[i])
        i+=1
    return result
    
def parse(expression):
    result=[]
    temp=""
    for x in expression:
        if x in ('*','+','-'):
            result.append(temp)
            result.append(x)
            temp=""
        else: temp+=x
    result.append(temp)
    return result