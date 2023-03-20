def solution(k, dungeons):
    n=len(dungeons)
    used=[0]*n
    
    answer = 0
    
    def choice(count, total, now):
        nonlocal answer
        if count==n:
            answer=max(answer,total)
            return
        choice(count+1, total, now)
        for i in range(n):
            if not used[i]:
                need, consume = dungeons[i]
                if now>=need:
                    used[i]=1
                    choice(count+1, total+1, now-consume)
                    used[i]=0
    
    choice(0,0,k)
    return answer