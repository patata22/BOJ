def solution(my_string):
    answer = 0
    temp=""
    for x in my_string:
        if x.isdigit():temp+=x
        else:
            if temp: answer+=int(temp)
            temp=""
    if temp: answer+=int(temp)
        

    return answer