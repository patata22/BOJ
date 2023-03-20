def solution(n, words):
    N=len(words)
    record=set()
    answer = [0,0]
    
    before=words[0]
    record.add(words[0])
    count=0
    for i in range(1,N):
        count+=1
        now = words[i]
        if now[0]!=before[-1] or now in record:
            answer=[count%n+1, count//n+1]
            break
        record.add(now)
        before=now

    return answer