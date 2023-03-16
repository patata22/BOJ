def solution(balls, share):
    return factorial(balls)/((factorial(balls-share))*factorial(share))

def factorial(n):
    if n<1: return 1
    if n in record:return record[n]
    else:
        record[n]=n*factorial(n-1)
        return record[n]
    


record={}
