def solution(babbling):
    answer = 0
    for b in babbling:
        if not check(b): answer+=1
    return answer

def check(b):
    for x in word:
        b=b.replace(x*2, 'x')
        b=b.replace(x,'!')
    b=b.replace('!','')
    return b

word=("aya", "ye", "woo", "ma")