def solution(nums):
    var=set(nums)
    return min(len(nums)//2, len(var))