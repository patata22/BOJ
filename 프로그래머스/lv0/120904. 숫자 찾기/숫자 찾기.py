def solution(num, k):
    try:
        return str(num).index(str(k))+1
    except ValueError: return -1
    