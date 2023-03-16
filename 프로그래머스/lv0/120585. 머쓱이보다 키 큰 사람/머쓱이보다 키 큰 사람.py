def solution(array, height):
    array.sort(reverse=True)
    i=0
    while i<len(array):
        if array[i]<=height: break
        i+=1
    return i