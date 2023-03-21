def solution(n, info):
    answer = [-1]
    info=info[::-1]
    myShot=[0]*11
    maxGap=0
    zeroShot=0
    
    def Shot(leftShot):
        nonlocal maxGap, zeroShot, answer
        gap = calcScore(info, myShot)
        if gap>maxGap:
            maxGap=gap
            zeroShot=leftShot
            answer=myShot[::-1]
        elif gap==maxGap and leftShot>zeroShot:
            zeroShot=leftShot
            answer=myShot[::-1]
        
        for i in range(1,11):
            if info[i]>=myShot[i]:
                temp = info[i]-myShot[i]+1
                if temp<=leftShot:
                    myShot[i]+=temp
                    Shot(leftShot-temp)
                    myShot[i]-=temp
    
    def calcScore(info, myShot):
        gap=0
        for i in range(1,11):
            if info[i]>myShot[i]: gap-=i
            elif info[i]<myShot[i]: gap+=i
        return gap
    
    Shot(n)
    if maxGap: answer[-1]=zeroShot
    return answer