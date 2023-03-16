def solution(a, b, n):
    answer = 0
    coke= n//a + n%a
    while n>=a:
        answer+=(n//a)*b
        n= (n//a)*b + n%a
        
    return answer