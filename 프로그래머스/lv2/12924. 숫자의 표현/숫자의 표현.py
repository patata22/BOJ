def solution(n):
    n*=2
    answer=0
    for i in range(1,int(n**0.5)+1):
        if not n%i and (n//i - i +1)%2==0: answer+=1
    return answer

