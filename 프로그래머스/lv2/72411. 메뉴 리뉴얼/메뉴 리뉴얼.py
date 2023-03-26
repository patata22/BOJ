def solution(orders, course):
    answer = []
    record=[{} for i in range(27)]
    
    def choice(count,now,n,order,part):
        if count==n:     
            if part not in record[n]:
                record[n][part]=1
            else: record[n][part]+=1
            return
        for i in range(now+1,len(order)):
            if not used[i]:
                used[i]=1
                choice(count+1, i, n,order, part+order[i])
                used[i]=0
    for order in orders:
        order=sorted(list(order))
        used=[0]*len(order)
        for n in course:
            choice(0,-1,n,order,"")
    
    for n in course:
        temp=0
        for x in record[n]:
            temp=max(temp,record[n][x])
        if temp>1:
            for x in record[n]:
                if record[n][x]==temp:
                    answer.append(x)
    answer.sort()
    return answer