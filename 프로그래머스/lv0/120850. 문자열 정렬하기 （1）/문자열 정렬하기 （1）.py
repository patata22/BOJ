def solution(my_string):
    answer = []
    for x in my_string:
        if x.isdigit(): answer.append(int(x))
    answer.sort()
    return answer