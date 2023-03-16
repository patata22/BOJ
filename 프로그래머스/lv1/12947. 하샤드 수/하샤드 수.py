def solution(x):
    div=0
    y=x
    while y:
        div+=y%10
        y//=10 
    answer=False if x%div else True
    return answer