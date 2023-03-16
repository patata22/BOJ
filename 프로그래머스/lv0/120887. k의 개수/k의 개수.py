def solution(i, j, k):
    k=str(k)
    answer = 0
    for l in range(i,j+1):
        answer+=str(l).count(k)
    
    return answer