def solution(numbers):
    stack=[]
    answer = []
    while numbers:
        now=numbers.pop()
        while stack and stack[-1]<=now:
            stack.pop()
        if not stack:
            answer.append(-1)
            
        else:
            answer.append(stack[-1])
        stack.append(now)
            
    return answer[::-1]