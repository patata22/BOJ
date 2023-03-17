def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    set1,set2={},{}
    
    for i in range(len(str1)-1):
        sub=str1[i:i+2]
        if validate(sub):
            if sub in set1: set1[sub]+=1
            else: set1[sub]=1
    for i in range(len(str2)-1):
        sub=str2[i:i+2]
        if validate(sub):
            if sub in set2: set2[sub]+=1
            else: set2[sub]=1
        
    kyo=0
    hap=0
    for x in set1:
        if x in set2:
            kyo+=min(set1[x],set2[x])
            hap+=max(set1[x],set2[x])
        else: hap+=set1[x]
    for x in set2:
        if x not in set1:
            hap+=set2[x]
    
    if not kyo and not hap: return 65536
    return int(65536*kyo/hap)


def validate(sub):
    if sub[0].isalpha() and sub[1].isalpha(): return True
    return False
