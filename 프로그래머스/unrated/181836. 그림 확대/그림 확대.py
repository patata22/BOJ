def solution(picture, k):
    answer = []
    for x in picture:
        temp=''
        for y in x:
            temp+=y*k
        for i in range(k):
            answer.append(temp)
    return answer