def solution(routes):
    routes.sort()
    right=-float('inf')
    answer = 0
    for start, end in routes:
        if start>right:
            right=end
            answer+=1
        else: right=min(right,end)
    return answer