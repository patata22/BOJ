def solution(A, B):
    answer = 0
    count = 0
    l=len(A)
    while A!=B and count<l:
        count+=1
        A= A[-1]+A[0:l-1]
    answer = count if A==B else -1
    return answer