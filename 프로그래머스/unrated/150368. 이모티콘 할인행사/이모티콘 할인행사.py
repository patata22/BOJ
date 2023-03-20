def solution(users, emoticons):
    n=len(emoticons)
    m=len(users)
    maxMember=0
    maxSales=0
    
    discount=[0]*n
    
    def decideDiscount(now):
        nonlocal maxMember, maxSales
        if now==n:
            member, sales = calcResult()
            if member>maxMember:
                maxMember= member
                maxSales = sales
            elif member==maxMember:
                maxSales = max(sales, maxSales)
            return
        
        for i in (10,20,30,40):
            discount[now]=i
            decideDiscount(now+1)
            
    def calcResult():
        member=0
        sales=0
        for dis,criteria in users:
            cost=0
            for i in range(n):
                if discount[i]>=dis:              
                    cost+= emoticons[i]*(100-discount[i])//100
            if cost>=criteria:member+=1
            else: sales+=cost
        return member, sales
    
    decideDiscount(0)
    
    return maxMember, maxSales