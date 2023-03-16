def solution(strings, n):
    strings.sort(key=lambda x: (ord(x[n]),x))
    return strings