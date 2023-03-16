def solution(participant, completion):
    start={}
    end={}
    
    for x in participant: 
        if x not in start:start[x]=1
        else: start[x]+=1
    for x in completion:
        if x not in end:end[x]=1
        else: end[x]+=1
    
    for x in participant:
        try:
            if start[x]!=end[x]:return x
        except KeyError: return x