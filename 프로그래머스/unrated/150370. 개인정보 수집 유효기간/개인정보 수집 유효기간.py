def solution(today, terms, privacies):
    n=len(privacies)
    answer = []
    record={}
    for term in terms:
        name,long=term.split()
        record[name]=int(long)*28
    
    todayToDay=changeToDay(today)
    
    for i in range(n):
        startDay, name = privacies[i].split()
        limitDay= record[name]+changeToDay(startDay)
        if limitDay<=todayToDay:answer.append(i+1)
        
        print(limitDay, todayToDay)
    print(record)
    
    
    
    return answer


def changeToDay(date):
    total=0
    year,month,day=map(int,date.split('.'))
    total+=(year-2000)*12*28
    total+=(month-1)*28
    total+=(day-1)
    return total

