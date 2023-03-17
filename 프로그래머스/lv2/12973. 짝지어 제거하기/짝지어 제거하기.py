def solution(s):
    stack=[]
    for x in s:
        if stack and stack[-1]==x:stack.pop()
        else: stack.append(x)
    answer=0 if stack else 1
    return answer