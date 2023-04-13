def solution(targets):
    targets.sort()
    answer = 0
    l,r=-1,-1
    for s,e in targets:
        if r<=s:
            l,r=s,e
            answer+=1
        else:
            l=s
            r=min(r,e)
    return answer