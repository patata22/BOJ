def solution(lottos, win_nums):
    count=0
    for x in lottos:
        if x in win_nums:count+=1
    zero=lottos.count(0)
    answer=[rank(count+zero), rank(count)]
    return answer

def rank(n):
    if n>=2: return 7-n
    else:return 6   