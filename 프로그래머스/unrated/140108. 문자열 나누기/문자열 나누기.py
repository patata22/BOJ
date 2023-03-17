def solution(s):
    answer = 0
    
    target=s[0]
    target_count=1
    etc_count=0
    idx=1
    while idx<len(s):
        if not target: target= s[idx]
        if s[idx]==target: target_count+=1
        else: etc_count+=1
        if target_count==etc_count:
            print(idx)
            answer+=1
            target_count=0
            etc_count=0
            target=""
        idx+=1
    if target_count:answer+=1
    return answer