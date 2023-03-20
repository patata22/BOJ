def solution(word):
    dictionary=set()
    vowel = ("A","E","I","O","U")
    
    def makeWord(count, now):
        if count==5:
            if now not in dictionary:
                dictionary.add(now)
            return
        makeWord(count+1, now)
        for v in vowel:
            makeWord(count+1, now+v)
    makeWord(0,"")
    
    dictionary=sorted(list(dictionary))
    return dictionary.index(word)