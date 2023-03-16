def solution(s):
    if len(s) not in (4,6):return False
    for x in s:
        if not x.isdigit():return False
    return True