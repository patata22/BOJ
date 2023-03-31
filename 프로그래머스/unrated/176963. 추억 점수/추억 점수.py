def solution(name, yearning, photo):
    answer=[]
    score={}
    for i in range(len(name)):
        score[name[i]]=yearning[i]
    for p in photo:
        temp=0
        for name in p:
            if name in score: temp+=score[name]
        answer.append(temp)
    return answer