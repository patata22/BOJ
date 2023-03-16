def solution(lines):
    count=[0]*202
    for start,end in lines:
        start+=101
        end+=101
        for i in range(start+1, end+1):
            count[i]+=1
    
    answer = 0
    
    for i in range(202):
        if count[i]>=2:answer+=1
    return answer