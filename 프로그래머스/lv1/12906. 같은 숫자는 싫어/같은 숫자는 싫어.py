def solution(arr):
    n=len(arr)
    answer=[arr[0]]
    for i in range(1,n):
        if arr[i]==answer[-1]: continue
        else: answer.append(arr[i])
    return answer