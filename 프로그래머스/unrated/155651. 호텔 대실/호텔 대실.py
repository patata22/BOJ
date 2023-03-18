def solution(book_time):
    
    occupied= [0]*1500
    
    for startTime, endTime in book_time:
        startTime = changeToMinute(startTime)
        endTime = changeToMinute(endTime)+10
        for i in range(startTime, endTime):
            occupied[i]+=1
        
    return max(occupied)

def changeToMinute(time):
    h,m=map(int,time.split(':'))
    return 60*h+m