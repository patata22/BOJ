def solution(s):
    answer = ''
    flag=False
    for x in s:
        if x==' ':
            flag=False
            answer+=x
        elif not flag:
            if x.isalpha:answer+=x.upper()
            else: answer+=x
            flag=True
        else: answer+=x.lower()
    return answer