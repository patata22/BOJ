import sys
sys.setrecursionlimit(10**6)

def solution(plans):
    answer = []
    n=len(plans)
    for plan in plans:
        plan[1]=parseTime(plan[1])
        plan[2]=int(plan[2])
    plans.sort(key=lambda x: x[1])
    isDone=[0]*n
    
    def doHomework(i):
        name, startTime, costTime = plans[i]
        for j in range(i+1, n):
            if not isDone[j]:
                if plans[j][1]<startTime+costTime:
                    costTime-= plans[j][1]-startTime                    
                    finishTime = doHomework(j)                
                    startTime = finishTime
                else: break
        isDone[i]=1
        answer.append(name)
        return startTime+costTime
    
    for i in range(n):
        if not isDone[i]:
            doHomework(i)
    
    return answer

def parseTime(time):
    h,m=map(int,time.split(':'))
    return 60*h+m