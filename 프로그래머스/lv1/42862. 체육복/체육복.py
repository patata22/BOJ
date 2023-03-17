def solution(n, lost, reserve):
    lost.sort()
    borrowable=[0]*(n+2)
    lostAndReserve=set()
    count=0
    
    for r in reserve: 
        if r in lost:
            lostAndReserve.add(r)
            count+=1
        else:borrowable[r]=1
        
    for i in range(len(lost)):
        now = lost[i]
        if now in lostAndReserve: continue
        elif borrowable[now-1]:
            borrowable[now-1]=0
            count+=1
            continue
        elif borrowable[now+1]:
            borrowable[now+1]=0
            count+=1
    return n-len(lost)+count
            
        
        
        