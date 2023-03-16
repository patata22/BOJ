def solution(polynomial):
    x=0
    n=0
    for p in polynomial.split(' + '):
        if 'x' in p:
            temp = p.strip('x')
            if not temp: x+=1
            else: x+=int(temp)
        else: n+=int(p)
    answer=''
    if x>1: answer+=str(x)
    if x: answer+='x'
    if answer and n: answer+= ' + '
    if n: answer+=str(n)
    return answer
    