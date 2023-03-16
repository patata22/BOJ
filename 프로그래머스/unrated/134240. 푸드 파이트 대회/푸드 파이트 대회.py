def solution(food):
    answer = ''
    n=len(food)
    for i in range(n-1,0,-1):
        answer+=str(i)*(food[i]//2)
    answer=answer[::-1]+'0'+answer
    
    return answer