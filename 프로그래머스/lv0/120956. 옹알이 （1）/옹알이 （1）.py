def solution(babbling):
    answer = 0
    comb(0,"")
    for b in babbling:
        if b in word: answer+=1
        
    return answer

def comb(count, com):
    if count==4: 
        if com: word.add(com)
        return
    for i in range(4):
        if not used[i]:
            used[i]=1
            comb(count+1,com+able[i])
            comb(count+1,com)
            used[i]=0

word=set()
able = ["aya", "ye", "woo", "ma"]
used=[0]*4

        

    