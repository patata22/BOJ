def solution(keymap, targets):
    count={}
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in count: count[key[i]]=i+1
            else: count[key[i]]= min(count[key[i]],i+1)
    answer = []
    for target in targets:
        temp = 0
        for x in target:
            if x not in count:
                temp=-1
                break
            else: temp+=count[x]
        answer.append(temp)
    return answer