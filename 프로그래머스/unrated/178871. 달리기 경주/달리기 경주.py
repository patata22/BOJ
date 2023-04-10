def solution(players, callings):
    n=len(players)
    index={}
    for i in range(n):
        index[players[i]]=i
    
    for call in callings:
        origin=index[call]
        target=index[call]-1
        targetName=players[target]
        players[origin], players[target]=players[target],players[origin]
        index[call]-=1
        index[targetName]+=1
    return players