def solution(quiz):
    answer = []
    for q in quiz:
        answer.append('O') if eval(q.replace('=', '==')) else answer.append('X')
        
    
    return answer