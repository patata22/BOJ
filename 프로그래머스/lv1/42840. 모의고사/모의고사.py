def solution(answers):
    n=len(answers)
    answer = []
    marking=[[1,2,3,4,5]*(n//5+1),[2,1,2,3,2,4,2,5]*(n//8+1),[3,3,1,1,2,2,4,4,5,5]*(n//10+1)]
    count=[0,0,0]
    for i in range(n):
        for j in range(3):
            if marking[j][i]==answers[i]:
                count[j]+=1
    for i in range(3):
        if count[i]==max(count): answer.append(i+1)
    return answer