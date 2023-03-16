def solution(number):
    global answer
    answer = 0
    
    def choice(count, now,total):
        global answer
        if count==3:
            if not total: answer+=1
            return
        for i in range(now,len(number)):
            choice(count+1, i+1, total+number[i])
    
    choice(0,0,0)
    
    return answer