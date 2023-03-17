def solution(progresses, speeds):
    progresses=progresses[::-1]
    speeds=speeds[::-1]
    answer = []
    day=0
    while progresses:
        head=progresses.pop()
        speed=speeds.pop()
        temp = head+speed*day
        day+=(100-temp)//speed
        if (100-temp)%speed:day+=1   
        answer.append(1)     
        for i in range(len(progresses)):
            if progresses[-1]+day*(speeds[-1])>=100:
                progresses.pop()
                speeds.pop()
                answer[-1]+=1
            else: break
    return answer