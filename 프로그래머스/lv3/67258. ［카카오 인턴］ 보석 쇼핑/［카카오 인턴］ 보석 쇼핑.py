def solution(gems):
    answer_length=float('inf')
    count={}
    name=set(gems)
    total=len(name)
    get=0
    for n in name: count[n]=0
    l,r=0,-1
    while r<len(gems)-1:
        if get<total:
            r+=1
            if not count[gems[r]]:
                get+=1
            count[gems[r]]+=1
        else:
            count[gems[l]]-=1
            if not count[gems[l]]:
                if r-l<answer_length:
                    answer_length=r-l
                    answer=[l+1,r+1]
                get-=1
            l+=1
    while get==total:
        count[gems[l]]-=1
        if not count[gems[l]]:
            if r-l<answer_length:
                answer_length=r-l
                answer=[l+1,r+1]
            get-=1
        l+=1
            
    return answer
