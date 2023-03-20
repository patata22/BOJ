def solution(clothes):
    count={}
    for cloth, type in clothes:
        if type not in count: count[type]=1
        else: count[type]+=1
    answer = 1
    print(count)
    for type in count:
        answer*= (count[type]+1)
    return answer-1