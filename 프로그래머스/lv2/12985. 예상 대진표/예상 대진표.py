def solution(n,a,b):
    if a>b: a,b=b,a
    answer=1
    while not a%2 or b%2 or a+1!=b:
        a=(a+1)//2
        b=(b+1)//2
        answer+=1
    return answer