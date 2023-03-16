def solution(my_string):
    return ''.join(sorted(list(map(lambda x: x.lower(), my_string))))
    