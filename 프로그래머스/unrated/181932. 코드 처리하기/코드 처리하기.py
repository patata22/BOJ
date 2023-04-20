def solution(code):
    mode=0
    answer=''
    for i in range(len(code)):
        x=code[i]
        if x=='1': mode=1-mode
        else:
            if mode and i%2: answer+=x
            elif not mode and not i%2: answer+=x
    if not answer:return 'EMPTY'
    return answer