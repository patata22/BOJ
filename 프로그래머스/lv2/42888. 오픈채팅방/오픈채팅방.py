def solution(record):
    name={}
    for r in record:
        temp=r.split()
        if temp[0] in ('Enter', 'Change'): name[temp[1]]=temp[2]
        
    answer = []
    for r in record:
        temp=r.split()
        if temp[0]=='Enter': answer.append(name[temp[1]]+"님이 들어왔습니다.")
        elif temp[0]=='Leave': answer.append(name[temp[1]]+"님이 나갔습니다.")
    
    return answer