def solution(my_string):
    answer = ''
    record=set()
    for x in my_string:
        if x not in record:
            answer+=x
            record.add(x)
    
    return answer