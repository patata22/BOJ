def solution(n):
    answer = n-1
    isPrime=[1]*(n+1)
    for i in range(2,n+1):
        if isPrime[i]:
            answer-=1
            for j in range(i+i,n+1,i):
                isPrime[j]=0
    return answer

