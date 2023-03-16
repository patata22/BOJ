def solution(numbers, k):
    now=0
    n=len(numbers)
    count=1
    while count<k:
        now=(now+2)%n
        count+=1
    return numbers[now]