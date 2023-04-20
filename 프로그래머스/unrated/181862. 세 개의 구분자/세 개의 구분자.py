def solution(myStr):
    s=myStr.replace('b','a')
    s=s.replace('c','a')
    s=s.split('a')
    answer=[]
    for x in s:
        if x: answer.append(x)
    if not answer:return ["EMPTY"]
    return answer
    