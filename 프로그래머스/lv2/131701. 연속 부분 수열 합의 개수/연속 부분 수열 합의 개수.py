from collections import deque

def solution(elements):
    n=len(elements)
    answer=set()
    elements=deque(elements)
    for i in range(n):
        elements.rotate()
        total=0
        for j in range(n):
            total+=elements[j]
            answer.add(total)
    return len(answer)