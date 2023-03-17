def solution(id_list, report, k):
    
    answer = []
    record={}
    count={}
    for id in id_list:
        record[id]=set()
        count[id]=0
    
    for r in report:
        reporter,target=r.split()
        if target not in record[reporter]:
            record[reporter].add(target)
            count[target]+=1
    
    for id in id_list:
        answer.append(0)
        for target in record[id]:
            if count[target]>=k:
                answer[-1]+=1
        
    return answer