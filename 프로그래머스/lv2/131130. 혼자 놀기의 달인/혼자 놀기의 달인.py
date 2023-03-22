def solution(cards):
    n=len(cards)
    cards=[0]+cards
    visited=[0]*(n+1)
    answer = [0]
    def travel(now,total):
        nonlocal answer
        to=cards[now]
        if not visited[to]:
            visited[to]=1
            travel(to,total+1)
            return
        answer.append(total)
    
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=1
            travel(i,1)
    answer.sort()
    return answer[-1]*answer[-2]