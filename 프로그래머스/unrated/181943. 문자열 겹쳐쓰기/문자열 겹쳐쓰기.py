def solution(my_string, over, s):
    a=list(my_string)
    b=list(over)
    a[s:s+len(b)]=b
    return ''.join(a)