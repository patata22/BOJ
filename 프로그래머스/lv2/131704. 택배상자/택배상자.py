def solution(order):
    n=len(order)
    answer,now=0,0
    box=[i for i in range(n,0,-1)]
    stack=[]
    while now<n:
        target=order[now]
        if box and box[-1]==target:
            box.pop()
            answer+=1
            now+=1
        elif stack and stack[-1]==target:
            stack.pop()
            answer+=1
            now+=1
        else:
            if box: stack.append(box.pop())
            else: break
        
    return answer