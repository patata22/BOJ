def solution(cards1, cards2, goal):
    cards1=cards1[::-1]
    cards2=cards2[::-1]
    goal=goal[::-1]
    
    while goal:
        now = goal.pop()
        if cards1 and cards1[-1]==now:
            cards1.pop()
            continue
        elif cards2 and cards2[-1]==now:
            cards2.pop()
            continue
        return 'No'
        
    return 'Yes'