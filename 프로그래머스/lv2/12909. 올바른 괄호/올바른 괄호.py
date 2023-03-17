def solution(s):
    pair={")":"(","}":"{", "]":"["}
    stack=[]
    for x in s:
        if x in pair:
            if stack and stack[-1]==pair[x]:stack.pop()
            else: return False
        else: stack.append(x)
    if stack: return False
    return True