from collections import deque

def solution(s):
    answer=0
    s=deque(s)
    l=len(s)
    for _ in range(l):
        s.append(s.popleft())
        answer+=check(s.copy())
    return answer

def check(s):
    pair={'[':']', '{':'}', '(':')'}
    stack=[]
    while s:
        x=s.pop()
        if x in pair:
            if stack and stack[-1]==pair[x]:stack.pop()
            else: return 0
        else: stack.append(x)
    if not stack: return 1
    else: return 0
