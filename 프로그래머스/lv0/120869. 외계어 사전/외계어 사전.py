def solution(spell, dic):
    global used
    n=len(spell)
    used=[0]*n
    
    comb(0,"",n,spell)
    for x in dic:
        if x in result: return 1
    return 2

def comb(count, word,n,spell):
    if count==n:
        result.add(word)
        return
    for i in range(n):
        if not used[i]:
            used[i]=1
            comb(count+1, word+spell[i],n,spell)
            used[i]=0
        
result=set()
