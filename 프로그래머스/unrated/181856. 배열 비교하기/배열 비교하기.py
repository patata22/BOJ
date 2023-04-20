def solution(arr1, arr2):
    a,b=len(arr1),len(arr2)
    if a>b: return 1
    if a<b: return -1
    if sum(arr1)>sum(arr2):return 1
    if sum(arr1)<sum(arr2):return -1
    return 0