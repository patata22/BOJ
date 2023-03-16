def solution(s):
    n=len(s)
    if n%2:return s[n//2]
    else: return s[n//2-1]+s[n//2]