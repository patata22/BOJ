def solution(begin, end):

    return [change(i) for i in range(begin, end+1)]
    

def change(n):
    if n==1: return 0
    temp=1
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            if n//i<=10000000:return n//i
            temp=i
    return temp
