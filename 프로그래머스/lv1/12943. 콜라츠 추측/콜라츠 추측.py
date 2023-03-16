def solution(num):
    answer = 0
    while answer<500 and num!=1:
        answer+=1
        if num%2: num=num*3+1
        else: num//=2
    if num==1: return answer
    else: return -1