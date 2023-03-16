def solution(n):
    answer = []
    sieve()
    for i in range(2,10001):
        if isPrime[i] and not n%i: answer.append(i)
    return answer


def sieve():
    for i in range(2,10001):
        if isPrime[i]:
            for i in range(i+i,10001,i):
                isPrime[i]=0

isPrime=[1]*10001
isPrime[1]=0
