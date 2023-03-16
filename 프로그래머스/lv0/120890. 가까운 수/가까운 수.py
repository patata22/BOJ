def solution(array, n):
    array.sort()
    temp=float('inf')
    answer = 0
    for x in array:
        gap=abs(n-x)
        if gap<temp:
            temp=gap
            answer=x
    
    return answer