def solution(my_string):
    answer = 0
    for x in my_string: answer+=change(x)
    return answer

def change(x):
    try: return int(x)
    except ValueError: return 0