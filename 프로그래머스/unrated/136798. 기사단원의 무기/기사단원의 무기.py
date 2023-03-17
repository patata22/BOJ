def solution(number, limit, power):
    count=[0]*(number+1)
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            count[j]+=1
    
    answer = 0
    
    for i in range(1,number+1):
        if count[i]>limit: answer+=power
        else: answer+=count[i]
    print(*count)
    return answer

