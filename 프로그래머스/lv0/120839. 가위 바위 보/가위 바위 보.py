def solution(rsp):
    win={'2':'0', '0':'5', '5':'2'}
    answer = ''
    for x in rsp:
        answer+=win[x]
    return answer