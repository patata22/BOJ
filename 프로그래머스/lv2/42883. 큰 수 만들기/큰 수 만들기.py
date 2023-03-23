def solution(number, k):
    number=list(map(int,list(number)))
    answer = []
    count=0
    for x in number:
        while answer and count<k and answer[-1]<x:
            count+=1
            answer.pop()
        answer.append(x)
    while len(answer)>len(number)-k:
        answer.pop()
    return ''.join(map(str,answer))