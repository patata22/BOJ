def solution(my_string):
    answer = ''
    for x in my_string:
        if x.islower():answer+=x.upper()
        else: answer+=x.lower()
    
    return answer